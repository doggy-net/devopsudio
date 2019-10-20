import re

from .. import GeneralDefaultMode, GeneralPriviledgeMode


class IOSDefaultCLIMode(GeneralDefaultMode):
    spec = {
        'login_prompt': 'Username: ',
        'username': 'admin',
        'password_prompt': 'Password: ',
        'password': 'pwdadmin',
        'error_prompts': [re.compile(br'% Login invalid')],
        'exit_command': ['exit'],
    }
    prompts = [re.compile(br'^\S+[>#]', re.M)]


class IOSEnableMode(GeneralPriviledgeMode):
    spec = {
        'enter_command': 'enable',
        'login_prompt': 'Username: ',
        'username': '',
        'password_prompt': 'Password: ',
        'password': 'enadmin',
        'error_prompts': [re.compile(br'^% Bad passwords')],
        'page_stopping_commands': ['terminal length 0', 'terminal width 512'],
        'exit_command': 'disable',
    }
    prompts = [re.compile(br'^\S+#', re.M)]
