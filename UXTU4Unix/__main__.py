from core import CPU, Shell

shell = Shell("070108")
dmi = shell.run("dmidecode -t processor")

cpu = CPU(dmi)

print(cpu.model_name)
print(cpu.family)
print(cpu.processor_type)
print(cpu.preferred_preset)