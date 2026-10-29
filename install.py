import os
import subprocess
import sys
from pathlib import Path


APP_DIR = Path(__file__).resolve().parent
VENV_DIR = Path.home() / ".venvs" / "ymd"
BIN_DIR = Path.home() / ".local" / "bin"


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def main() -> None:
    print("Installing YMD...")

    # Create a virtual environment
    run([sys.executable, "-m", "venv", str(VENV_DIR)])

    python = VENV_DIR / "bin" / "python"
    executable = VENV_DIR / "bin" / "ymd"

    # Install YMD and its dependencies
    run([str(python), "-m", "pip", "install", "-e", str(APP_DIR)])

    # Create the command directory
    BIN_DIR.mkdir(parents=True, exist_ok=True)

    # Create a symlink to the installed CLI
    launcher = BIN_DIR / "ymd"

    if launcher.exists() or launcher.is_symlink():
        launcher.unlink()

    launcher.symlink_to(executable)

    print("YMD installed successfully.")
    print("Run: ymd --help")

    if str(BIN_DIR) not in os.environ.get("PATH", "").split(os.pathsep):
        print(f'Add to PATH: export PATH="{BIN_DIR}:$PATH"')


if __name__ == "__main__":
    main()

