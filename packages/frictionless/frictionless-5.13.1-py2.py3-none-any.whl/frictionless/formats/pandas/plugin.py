from __future__ import annotations
from typing import TYPE_CHECKING
from ...system import Plugin
from .control import PandasControl
from .parser import PandasParser
from ...platform import platform
from ... import helpers

if TYPE_CHECKING:
    from ...resource import Resource


# NOTE:
# We need to ensure that the way we detect pandas dataframe is good enough.
# We don't want to be importing pandas and checking the type without a good reason


class PandasPlugin(Plugin):
    """Plugin for Pandas"""

    # Hooks

    def create_parser(self, resource):
        if resource.format == "pandas":
            return PandasParser(resource)

    def detect_resource(self, resource: Resource):
        if resource.data is not None:
            if helpers.is_type(resource.data, "DataFrame"):
                resource.format = resource.format or "pandas"
        if resource.format == "pandas":
            if resource.data is None:
                resource.data = platform.pandas.DataFrame()
            resource.datatype = resource.datatype or "table"
            resource.mediatype = resource.mediatype or "application/pandas"

    def select_control_class(self, type):
        if type == "pandas":
            return PandasControl
