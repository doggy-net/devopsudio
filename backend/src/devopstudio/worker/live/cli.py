from array import array
from telnetlib import Telnet
import re
import sys
import time


_CONN_TIMEOUT = 15  # Telnet init connection timeout
_RTRV_TIMEOUT = 5  # Telnet receive timeout
_URN_PMT = b'Username:'  # Prompt for username
_PWD_PMT = b'Password:'  # Prompt for password
_DFT_PMT = re.compile(rb'^\S+\s*(?:>)\s*$', re.M)  # Prompt after logging in
_PRI_PMT = re.compile(rb'^\S+\s*#\s*$', re.M)  # Prompt after logging in priviledge mode
_MORE_PMT = b'--More--'


class CLIMode:
    def __init__(self, ts, name, prompt):
        self.name = name
        self.prompt = prompt
        self.is_default = False
        self.__ts = ts

    def enter(self):
        self.__ts.send('enable\n')

    def exit(self):
        self.__ts.send('disable\n')


class TelnetSession:

    def __init__(self, host, port=23,
                 timeout=_CONN_TIMEOUT):
        self.__session = Telnet(host, port, timeout)
        self.__session.debuglevel = 0
        self.__loggedin = False
        self.__curr_mode = None
        self.__prompt = b''
        self.__config = {}

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def update_cfg(self, cfg):
        self.__config.update(cfg)

    def send(self, data, expected):
        if isinstance(data, str):
            data = data.encode()
        self.__session.write(data)
        return self.receive(expected)

    def receive(self, expected):
        index, match, data = self.__session.expect(
            expected, _RTRV_TIMEOUT)
        return index, match, data

    def login(self):
        if self.__loggedin:
            return True
        else:
            expected = [_URN_PMT, _PWD_PMT, _DFT_PMT]
            index, match, data = self.receive(expected)
            while True:
                if index == 0:
                    username = self.__config.get('username')
                    if not username:
                        return False
                    index, match, data = self.send(
                        username + '\n', expected)
                elif index == 1:
                    password = self.__config.get('password')
                    if not password:
                        return False
                    index, match, data = self.send(
                        password + '\n', expected)
                elif index == 2:
                    self.__prompt = match.group(0)
                    self.__loggedin = True
                    return True
                else:
                    raise Exception('Unexpected received text')

    def execute(self, command, cli_mode=None):
        if not self.login():
            return None
        rev = b''
        expected = [self.__prompt, b'--More--']
        index, _, data = self.send(command + '\n', expected)
        while True:
            if index == 0:
                rev += data
                rev = self.__prompt + rev
                return self.__handle_chr(rev)
            elif index == 1:
                rev += data
                index, _, data = self.send(' ', expected)
            else:
                break
        return None

    # Handle control character
    def __handle_chr(self, recv_text):
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
        self.__session.close()
