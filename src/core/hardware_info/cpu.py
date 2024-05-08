import re


def re_search(string: str, token: str) -> str:
    return re.search(f"(?<={token}: ).*", string)[0]


class CPU:
    def __init__(self, dmidecode_output: str):
        self.model = re_search(dmidecode_output, "Version")
        self.family = re_search(dmidecode_output, "Family")
