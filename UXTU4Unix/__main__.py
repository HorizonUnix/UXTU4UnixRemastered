import getpass
from argparse import ArgumentParser
from core import CPU, Shell


password = getpass.getpass(prompt=f"[sudo] password for hmm {getpass.getuser()}: ")

shell = Shell(password)
dmi = shell.run("dmidecode -t processor")

cpu = CPU(dmi)

print(cpu.model_name)
print(cpu.family)
print(cpu.processor_type)
print(cpu.preferred_preset)