import re

from enum import Enum, auto


class RyzenFamily(Enum):
    Unknown = -1
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


class ProcessorType(Enum):
    Unknown = -1
    AmdApu = auto()
    AmdDesktopCpu = auto()
    AmdLaptopCpu = auto()
    Intel = auto()


def search_for(input_string: str, token: str) -> str:  # Token: Result,
    return re.search(f"(?<={token} ).+?(?=,)", input_string)[0]


def get_family_name(model_name: str, signature: str) -> RyzenFamily:
    family = search_for(signature, "Family")
    model = search_for(signature, "Model")
    model_name = model_name.split()[3]  # AMD Ryzen X XXXXx

    match family:
        # Zen 1 - Zen 2
        case 23:
            match model:
                case 1:
                    return RyzenFamily.SummitRidge
                case 8:
                    return RyzenFamily.PinnacleRidge
                case 17 | 18:
                    return RyzenFamily.RavenRidge
                case 24:
                    return RyzenFamily.Picasso
                case 32:
                    if any(i in model_name for i in ('15e', '15Ce', '20e')):
                        return RyzenFamily.Pollock
                    else:
                        return RyzenFamily.Dali
                case 80:
                    return RyzenFamily.FireFlight
                case 96:
                    return RyzenFamily.Renoir
                case 104:
                    return RyzenFamily.Lucienne
                case 113:
                    return RyzenFamily.Matisse
                case 144:
                    return RyzenFamily.VanGogh
                case 160:
                    return RyzenFamily.Mendocino
        # Zen 3 - Zen 4
        case 25:
            match model:
                case 33:
                    return RyzenFamily.Vermeer
                case 63 | 68:
                    return RyzenFamily.Rembrandt
                case 80:
                    return RyzenFamily.CezanneBarcelo
                case 97:
                    if 'HX' in model_name:
                        return RyzenFamily.DragonRange
                    else:
                        return RyzenFamily.Raphael
                case 116:
                    return RyzenFamily.PhoenixPoint
                case 120:
                    return RyzenFamily.PhoenixPoint2
                case 117:
                    return RyzenFamily.HawkPoint
        # Zen 5 - Zen 6
        case 26:
            match model:
                case 32:
                    return RyzenFamily.StrixPoint
                case _:
                    return RyzenFamily.GraniteRidge


def get_processor_type(model_name: str, code_name: RyzenFamily) -> ProcessorType:
    if "Intel" in model_name:
        return ProcessorType.Intel

    match code_name:
        case RyzenFamily.SummitRidge | RyzenFamily.PinnacleRidge | RyzenFamily.Matisse | \
             RyzenFamily.Vermeer | RyzenFamily.Raphael | RyzenFamily.GraniteRidge:
            return ProcessorType.AmdDesktopCpu
        case _:
            return ProcessorType.AmdLaptopCpu
