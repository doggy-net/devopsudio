from enum import Enum, unique


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
    l2 = 'L2'
    L3IP4 = 'L3 IPv4'
    L3IP6 = 'L3 IPv6'
