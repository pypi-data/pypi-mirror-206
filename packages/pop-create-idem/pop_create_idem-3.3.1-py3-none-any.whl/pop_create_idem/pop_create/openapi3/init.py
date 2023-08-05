import pathlib
from typing import Dict

import openapi3.object_base
import requests
import yaml
from dict_tools.data import NamespaceDict


def context(hub, ctx, directory: pathlib.Path):
    if ctx.get("simple_service_name"):
        ctx.service_name = ctx.simple_service_name
    elif not ctx.get("service_name"):
        ctx.service_name = (
            ctx.clean_name.replace("idem", "").replace("cloud", "").strip("_")
        )

    ctx.has_acct_plugin = bool(ctx.acct_plugin)
    if not ctx.has_acct_plugin:
        # Create auth plugins
        ctx.acct_plugin = ctx.service_name

    # FIXME: Not an optimal way, it could take longer as for each spec we go through post generation hooks
    for specification in ctx.specification:
        # Read the spec from URL or local file (Yaml)
        spec = hub.pop_create.openapi3.init.read(source=specification)
        api = openapi3.OpenAPI(spec, validate=True)
        errors = api.errors()
        if errors:
            for e in errors:
                hub.log.warning(e)

        # list these as defaults in the acct plugin
        if api.servers:
            ctx.servers = [x.url for x in api.servers]
        else:
            ctx.servers = ctx.get("servers", [""])

        hub.log.debug(f"Working with openapi spec version: {api.openapi}")

        ctx.cloud_api_version = api.info.version or "latest"
        ctx.clean_api_version = hub.tool.format.case.snake(ctx.cloud_api_version).strip(
            "_"
        )

        if not ctx.clean_api_version:
            ctx.clean_api_version = ctx.get("clean_api_version")

        if not ctx.cloud_api_version:
            ctx.cloud_api_version = ctx.get("cloud_api_version")

        # If the api version starts with a digit then make sure it can be used for python namespacing
        if ctx.clean_api_version[0].isdigit():
            ctx.clean_api_version = "v" + ctx.clean_api_version

        # Get function plugins
        plugins = hub.pop_create.openapi3.parse.plugins(ctx, api)

        # Add any missing function which is required for idem resource modules
        plugins = hub.pop_create.openapi3.init.add_missing_known_functions(ctx, plugins)

        # Create request formats for function
        request_formats = hub.pop_create.openapi3.init.get_requests_formats(plugins)

        cloud_spec = NamespaceDict(
            api_version=ctx.cloud_api_version,
            project_name=ctx.project_name,
            service_name=ctx.service_name,
            request_format=request_formats,
            plugins=plugins,
        )
        ctx.cloud_spec = cloud_spec

        hub.pop_create.init.run(directory=directory, subparsers=["idem_cloud"], **ctx)

    return ctx


def read(hub, source: str or Dict):
    """
    If the path is a file, then parse the json contents of the file,
    If the path is a url, then return a json response from the url.
    """
    if isinstance(source, Dict):
        return source

    path = pathlib.Path(source)

    if path.exists():
        with path.open("r") as fh:
            ret = yaml.safe_load(fh)
    else:
        request = requests.get(source, headers={"Content-Type": "application/json"})
        ret = request.json()

    return ret


def get_requests_formats(hub, plugins):
    request_formats = {}

    request_formats["get"] = hub.pop_create.openapi3.template.GET_REQUEST_FORMAT
    request_formats["list"] = hub.pop_create.openapi3.template.LIST_REQUEST_FORMAT
    request_formats["create"] = hub.pop_create.openapi3.template.CREATE_REQUEST_FORMAT
    request_formats["update"] = hub.pop_create.openapi3.template.UPDATE_REQUEST_FORMAT
    request_formats["delete"] = hub.pop_create.openapi3.template.DELETE_REQUEST_FORMAT
    request_formats["present"] = hub.pop_create.openapi3.template.PRESENT_REQUEST_FORMAT
    request_formats["absent"] = hub.pop_create.openapi3.template.ABSENT_REQUEST_FORMAT
    request_formats[
        "describe"
    ] = hub.pop_create.openapi3.template.DESCRIBE_REQUEST_FORMAT

    for ref, func in plugins.items():
        for func_name, func_data in func["functions"].items():
            if func_name not in [
                "get",
                "list",
                "create",
                "update",
                "delete",
                "present",
                "absent",
                "describe",
            ]:
                request_formats[
                    func_name
                ] = hub.pop_create.openapi3.template.OTHER_FUNCTION_REQUEST_FORMAT

    return request_formats


def add_missing_known_functions(hub, ctx, plugins):
    # This is to make sure we still create standard skeletons for CRUD operations in exec
    # This way the only missing part would be API call in those modules
    for ref in list(plugins):
        for idem_func_name in ["get", "list", "create", "update", "delete"]:
            if not plugins[ref].get("functions", {}).get(idem_func_name):
                plugins[ref]["functions"][idem_func_name] = {
                    "doc": "",
                    "params": {},
                    "hardcoded": {
                        "method": "TODO",
                        "path": "TODO",
                        "service_name": ctx.service_name,
                        "resource_name": ref,
                    },
                }

    if ctx.create_plugin == "state_modules":
        for ref in list(plugins):
            for func_name in list(plugins.get(ref).get("functions", {})):
                if func_name == "create":
                    plugins[ref]["functions"]["present"] = (
                        plugins.get(ref).get("functions", {}).get(func_name)
                    )
                elif func_name == "delete":
                    plugins[ref]["functions"]["absent"] = (
                        plugins.get(ref).get("functions", {}).get(func_name)
                    )
                elif func_name == "list":
                    plugins[ref]["functions"]["describe"] = (
                        plugins.get(ref).get("functions", {}).get(func_name)
                    )

    return plugins
