from enum import Enum, unique


@unique
class ObjectType(Enum):
    ROUTER = 'Router'
    SWITCH = 'Siwtch'
    FIREWALL = 'Firewall'
    LOADBALANCER = 'Load Balancer'


@unique
class ExplorerNodeType(Enum):
    FOLDER = 'Folder'
    NODE = 'Node'


@unique
class GroupType(Enum):
    TILE = 'Tile'
    HIERARCHY = 'Hierarchy'


@unique
class LinkType(Enum):
    P2P = 'P2P'
    P2M = 'P2M'


@unique
class TopologyType(Enum):
    L2 = 'L2'
    L3IP4 = 'L3 IPv4'
    L3IP6 = 'L3 IPv6'
