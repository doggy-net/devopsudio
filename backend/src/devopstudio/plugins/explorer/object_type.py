from . import ExplorerBase, ExplorerNode
from devopstudio.utils.word import pluralize
from devopstudio.models.enums import ExplorerNodeType, ObjectType
from devopstudio.models.nom import NetworkObject


class ExplorerModule(ExplorerBase):
    name = 'Object Type'

    def run(self):
        for object_type in ObjectType:
            type_node = ExplorerNode(pluralize(object_type.value), ExplorerNodeType.FOLDER)
            network_objects = NetworkObject.objects.raw({'object_type': object_type.value})
            for no in network_objects:
                no_node = ExplorerNode(no.name, ExplorerNodeType.NODE)
                type_node.add_child(no_node)
            self.append(type_node)
