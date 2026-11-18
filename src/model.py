class ZoneTypes(enum):
    NORMAL = "normal"
    RESTRICTED = "restricted"
    PRIORITY = "priority"
    BLOCKED = "blocked"

class ZoneColors(enum):
    GOLD = "gold"
    BLACK = "black"
    RED = "red"
    DARKRED = "darkred"
    PURPLE = "purple"
    BROWN = "brown"
    MAROON = "maroon"
    ORANGE = "orange"
    CRIMSON = "crimson"
    RAINBOW = "rainbow"
    WHITE = "white"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    GRAY = "gray"
    VIOLET = "violet"

class Zone:
    name: str
    x: int
    y: int
    ztype: ZoneTypes
    color: ZoneColors
    max_drones: int

class Connection:
    zone_first: str
    zone_next: str
    max_link_capacity: int

class NetworkConfig:
    nb_drones: int
    start_hub: str
    end_hub: str
    hubs: list[Zone]
    connections: list[Connection]
