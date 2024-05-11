import re
from .ryzen_family import RyzenFamily

class CPU:
    def __init__(self, dmidecode_output: str):
        self.__dmidecode_output = dmidecode_output

        self.model = self.search_for("Version")
        self.clock_speed = self.search_for("Max Speed")
        self.core_count = self.search_for("Core Count")
        self.thread_count = self.search_for("Thread Count")

    @property
    def family(self) -> RyzenFamily:
        signature: list[str] = self.search_for("Signature").split(',')
        family: int = int(signature[1].split()[1])
        model: int = int(signature[2].split()[1])

        match family:
            # Zen 1 - Zen 2
            case 23:
                match model:
                    case 1: return RyzenFamily.SummitRidge
                    case 8: return RyzenFamily.PinnacleRidge
                    case 17 | 18: return RyzenFamily.RavenRidge
                    case 24: return RyzenFamily.Picasso
                    case 32:
                        if any(i in self.model for i in ["15e", "15Ce", "20e"]): return RyzenFamily.Pollock
                        else: return RyzenFamily.Dali
                    case 80: return RyzenFamily.FireFlight
                    case 96: return RyzenFamily.Renoir
                    case 104: return RyzenFamily.Lucienne
                    case 113: return RyzenFamily.Matisse
                    case 144: return RyzenFamily.VanGogh
                    case 160: return RyzenFamily.Mendocino
            # Zen 3 - Zen 4
            case 25:
                match model:
                    case 33: return RyzenFamily.Vermeer
                    case 63 | 68: return RyzenFamily.Rembrandt
                    case 80: return RyzenFamily.CezanneBarcelo
                    case 97:
                        if "HX" in self.model: return RyzenFamily.DragonRange
                        else: return RyzenFamily.Raphael
                    case 116: return RyzenFamily.PhoenixPoint
                    case 120: return RyzenFamily.PhoenixPoint2
                    case 117: return RyzenFamily.HawkPoint
            # Zen 5 - Zen 6
            case 26:
                match model:
                    case 32: return RyzenFamily.StrixPoint
                    case _: return RyzenFamily.GraniteRidge

    def search_for(self, token: str):
        return re.search(f"(?<={token}: ).*", self.__dmidecode_output)[0]
