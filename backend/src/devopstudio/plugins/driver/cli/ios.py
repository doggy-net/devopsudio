import re

from . import CLIDriverBase, GeneralDefaultMode, GeneralPriviledgeMode


class IOSDefaultCLIMode(GeneralDefaultMode):
    GeneralDefaultMode.update_spec({
        'login_prompt': 'Username: ',
        'username': 'admin',
        'password': 'pwdadmin',
        'login_error_prompts': [re.compile(br'% Login invalid')],
        'exit_command': ['exit'],
    })
    prompts = [re.compile(br'^\S+[>#]', re.M)]


class IOSEnableMode(GeneralPriviledgeMode):
    GeneralPriviledgeMode.update_spec({
        'enter_command': 'enable',
        'username': '',
        'password': 'enadmin',
        'login_error_prompts': [re.compile(br'^% Bad passwords')],
        'page_stopping_command': ['terminal length 0', 'terminal width 512'],
        'exit_command': 'disable',
    })
    prompts = [re.compile(br'^\S+#', re.M)]


class IOSDriver(CLIDriverBase):
    error_output = [
        re.compile(br'^% (Ambiguous|Incomplete|Invalid)', re.M),
    ]

    def __init__(self, *arg, **kwargs):
        self.reg_cli_mode(IOSDefaultCLIMode, default=True)
        self.reg_cli_mode(IOSEnableMode)
        super().__init__(*arg, **kwargs)
