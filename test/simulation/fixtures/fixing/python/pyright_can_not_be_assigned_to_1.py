# pyright: strict
from pathlib import Path
from typing import Optional, Tuple


def install_powershell() -> Path:
    return Path("/powershell")


def install(shell: Optional[str] = None) -> Tuple[str, Path]:
    if shell in {"powershell", None}:
        installed_path = install_powershell()
        return shell, installed_path
    else:
        raise RuntimeError("Error!")
