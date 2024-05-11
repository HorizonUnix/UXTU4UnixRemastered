from hardware_info import CPU
from shell_interaction import Shell

from typing import Final

LOCAL_VERSION: Final[str] = "0.2.9"


shell: Shell = Shell("070108")
dmi: str = shell.run("dmidecode -t processor")

cpu: CPU = CPU(dmi)
print(cpu.family)