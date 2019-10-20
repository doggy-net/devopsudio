from fnmatch import fnmatch
from netaddr import IPNetwork, IPRange
import re


class SelectorRule:

    def __init__(self, *, type=None, condition=None, driver=None, default=None):
        self._type = type or 'wildcards'
        self._condition = condition
        self._driver = driver
        self._default = default

    def match(self, value):
        if self._type == 'wildcards':
            if fnmatch(value, self._condition):
                return self._driver
        elif self._type == 'regex':
            if re.match(self._condition, value, re.I):
                return self._driver
        elif self._type == 'network':
            try:
                if '-' in self._condition:
                    if value in IPRange(*self._condition.split('-')):
                        return self._driver
                elif '/' in self._condition:
                    if value in IPNetwork(self._condition):
                        return self._driver
                else:
                    if value == self._condition:
                        return self._driver
            except:
                pass
        return self._default

class Selector:

    def __init__(self, rules, default=None):
        self._rules = load_rules(rules)
        self._default = default

    def match(self, ip):
        # This method is used to return a Driver type based on the kwargs
        # Return None if no matched Driver
        for rule in self._rules:
            matched_driver = rule.match(ip)
            if matched_driver:
                return matched_driver
        return self._default


def load_rules(rule_list):
    result_list = []
    for rule_dict in rule_list:
        result_list.append(SelectorRule(
            type=rule_dict.get('type'),
            condition=rule_dict.get('condition'),
            driver=rule_dict.get('driver'),
            default=rule_dict.get('default'),
        ))
    return result_list
