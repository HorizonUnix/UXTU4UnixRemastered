import re
from enum import Enum, auto


def camel_to_title(name: str) -> str:
    return " ".join(re.findall("[A-Z 2][^A-Z 2]*", name))


class RyzenFamily(Enum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list) -> str:
        return camel_to_title(name)

    Unknown = auto()
    SummitRidge = auto()
    PinnacleRidge = auto()
    RavenRidge = auto()
    Dali = auto()
    Pollock = auto()
    Picasso = auto()
    FireFlight = auto()
    Matisse = auto()
    Renoir = auto()
    Lucienne = auto()
    VanGogh = auto()
    Mendocino = auto()
    Vermeer = auto()
    CezanneBarcelo = auto()
    Rembrandt = auto()
    Raphael = auto()
    DragonRange = auto()
    PhoenixPoint = auto()
    PhoenixPoint2 = auto()
    HawkPoint = auto()
    SonomaValley = auto()
    GraniteRidge = auto()
    FireRange = auto()
    StrixPoint = auto()
    StrixPoint2 = auto()
    Sarlak = auto()


