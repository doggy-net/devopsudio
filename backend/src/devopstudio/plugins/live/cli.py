from array import array
from telnetlib import Telnet
import re
import sys
import time


_URN_PMT = b'Username:'  # Prompt for username
_PWD_PMT = b'Password:'  # Prompt for password
_DFT_PMT = re.compile(rb'^\S+\s*(?:%)\s*$', re.M)  # Prompt after logging in
_PRI_PMT = re.compile(rb'^\S+\s*#\s*$', re.M)  # Prompt after logging in priviledge mode
_MORE_PMT = b'--More--'


class UnexpectedCLIResponse(Exception):
    pass


class CLIMode:

    def __init__(self, ts, name, prompt):
        self.name = name
        self.prompt = prompt
        self.is_default = False
        self._ts = ts

    def enter(self):
        self._ts.send('enable\n')

    def exit(self):
        self._ts.send('disable\n')


class TelnetSession:

    def __init__(self, host, port=23,
                 timeout=15):
        self._session = Telnet(host, port, timeout)
        self._session.debuglevel = 0
        self._loggedin = False
        self._curr_mode = None
        self._prompt = b''
        self._config = {}

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def update_cfg(self, cfg):
        self._config.update(cfg)

    def send(self, data, expected):
        if isinstance(data, str):
            data = data.encode()
        self._session.write(data)
        return self.receive(expected)

    def receive(self, expected, timeout=5):
        index, match, data = self._session.expect(
            expected, timeout)
        if index == -1:
            raise UnexpectedCLIResponse(f'Unexpected received: {data}')
        return index, match, data

    def login(self):
        pass
        if self._loggedin:
            return True
        else:
            expected = [_URN_PMT, _PWD_PMT, _DFT_PMT]
            index, match, _ = self.receive(expected)
            while True:
                if index == 0:
                    username = self._config.get('username')
                    if not username:
                        return False
                    index, match, _ = self.send(
                        username + '\n', expected)
                elif index == 1:
                    password = self._config.get('password')
                    if not password:
                        return False
                    index, match, _ = self.send(
                        password + '\n', expected)
                elif index == 2:
                    self._prompt = match.group(0)
                    self._loggedin = True
                    return True

    def execute(self, command, cli_mode=None):
        if not self.login():
            return None
        rev = b''
        expected = [self._prompt, b'--More--', re.compile(rb'^% (Invalid|Ambiguous|Incomplete)', re.M)]
        index, _, data = self.send(command + '\n', expected)
        while True:
            if index == 0:
                rev += data
                rev = self._prompt + rev
                return self._handle_chr(rev)
            elif index == 1:
                rev += data
                index, _, data = self.send(' ', expected)
            else:
                break
        return None

    # Handle control character
    def _handle_chr(self, recv_text):
        recv_arr = array('b')
        recv_arr.frombytes(recv_text)
        new_arr = array('b')
        for recv in recv_arr:
            if recv == 8:  # [BS] (backspace)
                if new_arr:
                    new_arr.pop()
            else:
                new_arr.append(recv)
        return new_arr.tobytes().decode()

    def close(self):
        self._session.close()
