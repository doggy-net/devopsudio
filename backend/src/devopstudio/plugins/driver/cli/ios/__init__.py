import re

from .cli_modes import IOSDefaultCLIMode, IOSEnableMode
from .parsers import basic, software
from .. import CLIDriverBase


class DriverModule(CLIDriverBase):
    name = 'IOS Driver'
    error_prompts = [
        re.compile(br'^% (Ambiguous|Incomplete|Invalid)', re.M),
    ]
    cli_modes = {
        'default': IOSDefaultCLIMode,
        'priviledge': IOSEnableMode,
    }
    basic_parser = basic
    parsers = [software]
