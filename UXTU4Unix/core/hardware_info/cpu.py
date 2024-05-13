import re

from core.hardware_info.ryzen import RyzenFamily, ProcessorType, get_family_name, get_processor_type
from core.premade_presets.presets import Preset, get_preset


def search_for(input_string: str, token: str) -> str:  # Token: Result with Space
    return re.search(f"(?<={token}: ).*", input_string)[0]


class CPU:
    def __init__(self, dmidecode_processor_output: str) -> None:
        self.__dmidecode_processor_output = dmidecode_processor_output

        self.model_name = search_for(self.__dmidecode_processor_output, "Version")
        self.clock_speed = search_for(self.__dmidecode_processor_output, "Max Speed")
        self.voltage = search_for(self.__dmidecode_processor_output, "Voltage")
        self.core_count = search_for(self.__dmidecode_processor_output, "Core Count")
        self.thread_count = search_for(self.__dmidecode_processor_output, "Thread Count")
        self.signature = search_for(self.__dmidecode_processor_output, "Signature")

    @property
    def family(self) -> RyzenFamily:
        return get_family_name(self.model_name, self.signature)

    @property
    def processor_type(self) -> ProcessorType:
        return get_processor_type(self.model_name, self.family)

    @property
    def preferred_preset(self) -> Preset:
        return get_preset(self.model_name, self.processor_type, self.family)