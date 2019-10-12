from abc import ABCMeta, abstractmethod
from copy import deepcopy
from telnetlib import Telnet

from ._util import to_bytes


DEBUGGING = True


class Received:

    def __init__(self, index, match, data):
        self.index = index
        self.match = match
        self.data = data

    def __str__(self):
        return self.data

    def __bool__(self):
        return bool(self.match)


class CLIMode(metaclass=ABCMeta):
    spec = {}
    name = None
    prompt = None

    def __init__(self, session):
        self._session = session
        self.settings = deepcopy(self.spec)

    def update_settings(self, update):
        self.settings.update(update)

    @abstractmethod
    def enter(self):
        # This method is supposed to enter the CLI mode and return True/False
        # if enter the CLI mode successfully or not
        pass

    @abstractmethod
    def exit(self):
        # This method is supposed to exit the CLI mode
        pass


class GeneralDefaultMode(CLIMode):
    spec = {
        'login_prompt': 'login: ',
        'username': None,
        'password_prompt': 'Password: ',
        'password': None,
        'error_prompts': [],
        'exit_command': None,
    }
    name = 'default'
    prompts = []

    def enter(self):
        error_prompts_len = len(self.spec['error_prompts'])
        prompts_len = len(self.prompts)
        while True:
            recv = self._session.receive([*self.spec['error_prompts'], *self.prompts,
                                         self.spec['login_prompt'], self.spec['password_prompt']])
            if not recv:
                return False

            # Match login error prompts
            if recv.index < error_prompts_len:
                return False

            # Match prompts
            if recv.index < error_prompts_len + prompts_len:
                return True

            # Match login prompt
            if recv.index == error_prompts_len + prompts_len:
                username = self.spec.get('username')
                if not username:
                    return False
                self._session.send(username)
                continue

            # Match password prompt
            if recv.index == error_prompts_len + prompts_len + 1:
                password = self.spec.get('password')
                if not password:
                    return False
                self._session.send(password)
                continue

        return False


    def exit(self):
        self._session.send(self.spec['exit_command'])


class GeneralPriviledgeMode(CLIMode):
    name = 'priviledge'
    prompts = []
    spec = {
        'enter_command': None,
        'login_prompt': 'Username: ',
        'username': None,
        'password_prompt': 'Password: ',
        'password': None,
        'error_prompts': [],
        'page_stopping_commands': [],
        'exit_command': None,
    }

    def enter(self):
        self._session.send(self.spec['enter_command'])

        error_prompts_len = len(self.spec['error_prompts'])
        prompts_len = len(self.prompts)
        while True:
            recv = self._session.receive([*self.spec['error_prompts'], *self.prompts,
                                        self.spec['password_prompt']])
            if not recv:
                return False

            # Match login error prompts
            if recv.index < error_prompts_len:
                return False

            # Match prompts
            if recv.index < error_prompts_len + prompts_len:
                # execute page stopping commands
                for command in self.spec['page_stopping_commands']:
                    self._session.execute_command(command)
                return True

            # Match password prompt
            if recv.index == error_prompts_len + prompts_len:
                password = self.spec.get('password')
                if not password:
                    return False
                self._session.send(password)
                continue

        return False

    def exit(self):
        self._session.send(self.spec['exit_command'])


class CLIDriverBase(metaclass=ABCMeta):
    error_prompts = []
    cli_modes = {}

    def __init__(self, host, method='telnet', port=None, username=None, password=None, **kwargs):
        if method == 'telnet':
            if not port:
                port = 23
            self._connection = Telnet(host, port, timeout=60)
        elif method == 'ssh':
            if not port:
                port = 22
            raise NotImplementedError('Todo')
        else:
            raise ValueError("'method' musth be 'telnet' or 'ssh'")

        self._cli_modes = {name: self.cli_modes[name](self) for name in self.cli_modes}

        if not self._cli_modes:
            raise ValueError('No registered CLI modes found')
        elif 'default' not in self._cli_modes:
            raise ValueError('No default CLI mode found')

        self._curr_mode = None
        try:
            cli_mode = self._cli_modes['default']
            if cli_mode.enter():
                self._curr_mode = cli_mode
                self.prompts = cli_mode.prompts
            else:
                raise PermissionError('Login invalid')
        except Exception as ex:
            self.close()
            raise PermissionError(f"Failed to enter default CLI mode with exception '{ex}'")

        if 'priviledge' in self._cli_modes:
            try:
                cli_mode = self._cli_modes['priviledge']
                if cli_mode.enter():
                    self._curr_mode = cli_mode
                    self.prompts = cli_mode.prompts
            except:
                pass

    def send(self, data, send_enter=True):
        data = to_bytes(data)
        if send_enter:
            data += b'\r'
        if DEBUGGING:
            print(f'sent: {data.decode()}')
        self._connection.write(data)

    def receive(self, expected, timeout=5):
        expected = [to_bytes(exp)for exp in expected]
        index, match, data = self._connection.expect(
            expected, timeout)
        if DEBUGGING:
            print(f'received: {data.decode()}')
        if index == -1:
            raise ValueError(f'Unexpected response received: {data}, expect: {expected}')
        return Received(index, match, data)

    def execute_command(self, command, cli_mode_name=None, timeout=600):
        if not cli_mode_name:
            cli_mode = self._curr_mode
        else:
            cli_mode = self._cli_modes.get(cli_mode_name, self._curr_mode)
        expected = [*cli_mode.prompts, *self.error_prompts]
        self.send(command)
        recv = self.receive(expected, timeout)
        if recv.index < len(cli_mode.prompts):
            result = recv.match.group(0) + recv.data
            return result.decode()
        elif recv.index != -1 and cli_mode_name == 'default' and 'priviledge' in self._cli_modes:
            return self.execute_command(command, cli_mode_name='priviledge', timeout=timeout)
        return None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        if not self._curr_mode:
            pass
        elif self._curr_mode.name != 'default':
            self._curr_mode.exit()
            self._cli_modes['default'].exit()
        else:
            self._curr_mode.exit()
        self._connection.close()
