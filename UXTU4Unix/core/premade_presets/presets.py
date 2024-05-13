from dataclasses import dataclass

from core.hardware_info.ryzen import ProcessorType, RyzenFamily


@dataclass
class Preset:
    Eco: str
    Balance: str
    Performance: str
    Extreme: str
    AC: str = "--max-performance"
    DC: str = "--power-saving"


def get_preset(model_name: str, processor_type: ProcessorType, family: RyzenFamily) -> Preset:
    model_name = model_name.split()  # AMD Ryzen X XXXXx
    model = model_name[3]

    match processor_type:
        case ProcessorType.AmdApu:
            # Pre Matisse
            if family < RyzenFamily.Matisse:
                if any(i in model for i in ('U', 'e', 'Ce')):
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=6000 --fast-limit=8000 --stapm-time=64 --slow-limit=6000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=15000 --fast-limit=18000 --stapm-time=64 --slow-limit=16000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=18000 --fast-limit=20000 --stapm-time=64 --slow-limit=19000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=28000 --fast-limit=28000 --stapm-time=64 --slow-limit=28000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
                if 'H' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=6000 --fast-limit=8000 --stapm-time=64 --slow-limit=6000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=30000 --fast-limit=35000 --stapm-time=64 --slow-limit=33000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=35000 --fast-limit=42000 --stapm-time=64 --slow-limit=40000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=56000 --fast-limit=56000 --stapm-time=64 --slow-limit=56000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
                if 'GE' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=15000  --fast-limit=15000 --stapm-time=64 --slow-limit=18000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=45000  --fast-limit=55000 --stapm-time=64 --slow-limit=48000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=55000  --fast-limit=65000 --stapm-time=64 --slow-limit=60000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=65000  --fast-limit=80000 --stapm-time=64 --slow-limit=75000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
                if 'G' in model:
                    return Preset(
                        Eco="--tctl-temp=95 apu-skin-temp=45 --stapm-limit=15000  --fast-limit=18000 --stapm-time=64 --slow-limit=18000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=65000  --fast-limit=75000 --stapm-time=64 --slow-limit=65000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=80000  --fast-limit=75000 --stapm-time=64 --slow-limit=75000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=85000  --fast-limit=95000 --stapm-time=64 --slow-limit=90000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
            # Post Matisse
            if family > RyzenFamily.Matisse:
                if 'U' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=6000 --fast-limit=8000 --stapm-time=64 --slow-limit=6000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=22000 --fast-limit=24000 --stapm-time=64 --slow-limit=22000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=28000 --fast-limit=28000 --stapm-time=64 --slow-limit=28000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=30000 --fast-limit=34000 --stapm-time=64 --slow-limit=32000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
                if 'HX' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=6000 --fast-limit=8000 --stapm-time=64 --slow-limit=6000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=55000 --fast-limit=65000 --stapm-time=64 --slow-limit=55000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=78000 --fast-limit=70000 --stapm-time=64 --slow-limit=70000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=85000 --fast-limit=95000 --stapm-time=64 --slow-limit=90000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
                if 'HS' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=6000 --fast-limit=8000 --stapm-time=64 --slow-limit=6000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=35000 --fast-limit=45000 --stapm-time=64 --slow-limit=38000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=45000 --fast-limit=55000 --stapm-time=64 --slow-limit=50000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=55000 --fast-limit=70000 --stapm-time=64 --slow-limit=65000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
                if 'H' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=6000 --fast-limit=8000 --stapm-time=64 --slow-limit=6000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=45000 --fast-limit=55000 --stapm-time=64 --slow-limit=48000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=55000 --fast-limit=65000 --stapm-time=64 --slow-limit=60000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=65000 --fast-limit=80000 --stapm-time=64 --slow-limit=75000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
                if 'GE' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=15000 --fast-limit=15000 --stapm-time=64 --slow-limit=18000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=45000 --fast-limit=55000 --stapm-time=64 --slow-limit=48000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=55000 --fast-limit=65000 --stapm-time=64 --slow-limit=60000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=65000 --fast-limit=80000 --stapm-time=64 --slow-limit=75000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
                if 'G' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=15000 --fast-limit=18000 --stapm-time=64 --slow-limit=18000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=65000 --fast-limit=75000 --stapm-time=64 --slow-limit=65000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=80000 --fast-limit=75000 --stapm-time=64 --slow-limit=75000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=85000 --fast-limit=95000 --stapm-time=64 --slow-limit=90000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )
            # Mendocino
            if family == RyzenFamily.Mendocino:
                if 'U' in model:
                    return Preset(
                        Eco="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=6000 --fast-limit=8000 --stapm-time=64 --slow-limit=6000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Balance="--tctl-temp=95 --apu-skin-temp=45 --stapm-limit=15000 --fast-limit=18000 --stapm-time=64 --slow-limit=16000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Performance="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=18000 --fast-limit=20000 --stapm-time=64 --slow-limit=19000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                        Extreme="--tctl-temp=95 --apu-skin-temp=95 --stapm-limit=28000 --fast-limit=28000 --stapm-time=64 --slow-limit=28000 --slow-time=128 --vrm-current=180000 --vrmmax-current=180000 --vrmsoc-current=180000 --vrmsocmax-current=180000 --vrmgfx-current=180000",
                    )

        case ProcessorType.AmdDesktopCpu:
            if family < RyzenFamily.Raphael:
                if 'E' in model:
                    return Preset(
                        Eco="--tctl-temp=95",
                        Balance="--tctl-temp=95",
                        Performance="--tctl-temp=95",
                        Extreme="--tctl-temp=95",
                    )
                if 'X3D' in model:
                    return Preset(
                        Eco="--tctl-temp=85",
                        Balance="--tctl-temp=85",
                        Performance="--tctl-temp=85",
                        Extreme="--tctl-temp=85",
                    )
                if 'X' in model and '9' in model_name[2]:
                    return Preset(
                        Eco="--tctl-temp=95",
                        Balance="--tctl-temp=95",
                        Performance="--tctl-temp=95",
                        Extreme="--tctl-temp=95",
                    )
                if 'X' in model:
                    return Preset(
                        Eco="--tctl-temp=95",
                        Balance="--tctl-temp=95",
                        Performance="--tctl-temp=95",
                        Extreme="--tctl-temp=95",
                    )
            if family >= RyzenFamily.Raphael:
                if 'E' in model:
                    return Preset(
                        Eco="--tctl-temp=95",
                        Balance="--tctl-temp=95",
                        Performance="--tctl-temp=95",
                        Extreme="--tctl-temp=95",
                    )
                if 'X3D' in model:
                    return Preset(
                        Eco="--tctl-temp=85",
                        Balance="--tctl-temp=85",
                        Performance="--tctl-temp=85",
                        Extreme="--tctl-temp=85",
                    )
                if 'X' in model and '9' in model_name[2]:
                    return Preset(
                        Eco="--tctl-temp=95",
                        Balance="--tctl-temp=95",
                        Performance="--tctl-temp=95",
                        Extreme="--tctl-temp=95",
                    )
                # Other
                return Preset(
                    Eco="--tctl-temp=95",
                    Balance="--tctl-temp=95",
                    Performance="--tctl-temp=95",
                    Extreme="--tctl-temp=95",
                )
