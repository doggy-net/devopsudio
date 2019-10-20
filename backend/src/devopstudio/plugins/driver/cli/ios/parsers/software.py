import re

from devopstudio.models.nom import SoftwareDataModel
from devopstudio.plugins.driver.cli import CLIParserBase


class ParserModule(CLIParserBase):
    name = 'software'
    datamodel = SoftwareDataModel

    def run(self):
        version_outputs = self._driver.execute_command('show version')
        if not version_outputs:
            return None
        ver_re = re.search(r'Version ([^\s,]+)', version_outputs)
        if not ver_re:
            return None
        version = ver_re.group(1)
        self.data = self.datamodel(
            version=version,
        )
        return self.data
