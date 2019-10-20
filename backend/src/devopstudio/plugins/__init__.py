from abc import ABCMeta, abstractmethod


class PluginBase(metaclass=ABCMeta):

    def __init__(self):
        self._options = {}

    def get_option(self, option):
        return self._options.get(option)

    def set_option(self, option, value):
        self._options[option] = value

    @abstractmethod
    def run(self):
        pass
