from __future__ import annotations
from typing import TYPE_CHECKING
from ...system import Plugin
from ...detector import Detector
from .control import YamlControl
from .parser import YamlParser

if TYPE_CHECKING:
    from ...resource import Resource


class YamlPlugin(Plugin):
    """Plugin for Yaml"""

    # Hooks

    def create_parser(self, resource):
        if resource.format == "yaml":
            return YamlParser(resource)

    def detect_resource(self, resource: Resource):
        if resource.format == "yaml":
            resource.datatype = (
                resource.datatype
                or Detector.detect_metadata_type(resource.normpath, format="yaml")
                or "json"
            )
            resource.mediatype = resource.mediatype or "text/yaml"

    def select_control_class(self, type):
        if type == "yaml":
            return YamlControl
