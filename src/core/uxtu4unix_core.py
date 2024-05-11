from hardware_info import CPU
from shell_interaction import Shell

from typing import Final

LOCAL_VERSION: Final[str] = "0.2.9"


shell = Shell("070108")
dmi = shell.run("dmidecode -t processor")

cpu = CPU(dmi)
print(cpu.family)