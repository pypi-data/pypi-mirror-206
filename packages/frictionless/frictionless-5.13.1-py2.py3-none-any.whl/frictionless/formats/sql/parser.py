from __future__ import annotations
from typing import TYPE_CHECKING
from ...platform import platform
from ...exception import FrictionlessException
from ...system import Parser
from .control import SqlControl
from .adapter import SqlAdapter

if TYPE_CHECKING:
    from ...resources import TableResource


class SqlParser(Parser):
    """SQL parser implementation."""

    supported_types = [
        "boolean",
        "date",
        "datetime",
        "integer",
        "number",
        "string",
        "time",
    ]

    # Read

    def read_cell_stream_create(self):
        assert self.resource.normpath
        control = SqlControl.from_dialect(self.resource.dialect)
        if not control.table:
            raise FrictionlessException('Please provide "dialect.sql.table" for reading')
        engine = platform.sqlalchemy.create_engine(self.resource.normpath)
        adapter = SqlAdapter(engine, control=control)
        if not adapter:
            raise FrictionlessException(f"Not supported source: {self.resource.normpath}")
        if not self.resource.schema:
            self.resource.schema = adapter.read_schema(control.table)
        return adapter.read_cell_stream(control)

    # Write

    def write_row_stream(self, source: TableResource):
        assert self.resource.normpath
        control = SqlControl.from_dialect(self.resource.dialect)
        if not control.table:
            raise FrictionlessException('Please provide "dialect.sql.table" for writing')
        engine = platform.sqlalchemy.create_engine(self.resource.normpath)
        adapter = SqlAdapter(engine, control=control)
        if not adapter:
            raise FrictionlessException(f"Not supported source: {self.resource.normpath}")
        with source:
            adapter.write_schema(source.schema, table_name=control.table)
            adapter.write_row_stream(source.row_stream, table_name=control.table)
