from __future__ import annotations
import typer
from typing import List
from rich.console import Console
from ...resource import Resource
from ...system import system
from ..console import console
from .. import common
from .. import utils


@console.command(name="index")
def console_index(
    # Resource
    source: List[str] = common.source,
    name: str = common.resource_name,
    type: str = common.type,
    path: str = common.path,
    # Command
    database: str = common.database,
    fast: bool = common.fast,
    fallback: bool = common.fallback,
    qsv: str = common.qsv,
    # System
    debug: bool = common.debug,
    trusted: bool = common.trusted,
    standards: str = common.standards,
):
    """Index a tabular data resource"""
    console = Console()

    # Setup system
    if trusted:
        system.trusted = trusted
    if standards:
        system.standards = standards  # type: ignore

    # Create source
    source = utils.create_source(source, path=path)
    if not source and not path:
        note = 'Providing "source" or "path" is required'
        utils.print_error(console, note=note)
        raise typer.Exit(code=1)

    # Index resource
    console.rule("[bold]Index")
    try:
        # Create resource
        resource = Resource(
            source=utils.create_source(source),
            name=name,
            path=path,
            datatype=type,
        )

        # Index resources
        names = []
        resources = resource.list()
        for resource in resources:
            names.extend(
                utils.index_resource(
                    console,
                    resource=resource,
                    database=database,
                    fast=fast,
                    use_fallback=fallback,
                    qsv_path=qsv,
                    debug=debug,
                )
            )
    except Exception as exception:
        utils.print_exception(console, debug=debug, exception=exception)
        raise typer.Exit(code=1)

    # Print result
    console.rule("[bold]Result")
    console.print(f"Succesefully indexed [bold]{len(names)}[/] tables")
