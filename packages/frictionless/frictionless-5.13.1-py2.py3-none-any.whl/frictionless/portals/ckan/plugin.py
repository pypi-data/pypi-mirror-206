from __future__ import annotations
import re
from ...system import Plugin
from urllib.parse import urlparse
from .control import CkanControl
from .adapter import CkanAdapter


class CkanPlugin(Plugin):
    """Plugin for Ckan"""

    # Hooks

    # TODO: improve
    def create_adapter(self, source, *, control=None, basepath=None, packagify=False):
        if isinstance(source, str):
            parsed = urlparse(source)
            if not control or isinstance(control, CkanControl):
                if re.search(r"^/dataset/[^/]+$", parsed.path):
                    control = control or CkanControl()
                    if not control.baseurl:
                        baseurl, dataset = source.split("/dataset/")
                        control.baseurl = baseurl
                    else:
                        dataset = source.split("/dataset/")[1]
                    if dataset:
                        control.dataset = dataset
                elif control:
                    control.dataset = source

                if isinstance(control, CkanControl):
                    return CkanAdapter(control)
        if source is None and isinstance(control, CkanControl):
            return CkanAdapter(control)

    def select_control_class(self, type):
        if type == "ckan":
            return CkanControl
