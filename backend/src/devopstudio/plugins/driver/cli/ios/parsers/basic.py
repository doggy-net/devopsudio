import re

from devopstudio.models.enums import ObjectType
from devopstudio.models.nom import NetworkObject
from devopstudio.plugins.driver.cli import CLIParserBase


class ParserModule(CLIParserBase):
    name = 'basic'
    datamodel = NetworkObject

    def run(self):
        basic_outputs = self._driver.execute_command('')
        if not basic_outputs:
            return None
        name_re = re.search(r'^(\S+)[>#]', basic_outputs, re.M)
        if not name_re:
            return None
        name = name_re.group(1)
        self.data = self.datamodel(
            name=name,
            driver=self._driver.name,
            object_type=ObjectType.ROUTER,
            management_ip=self._driver._connection.host,
        )
        return self.data
