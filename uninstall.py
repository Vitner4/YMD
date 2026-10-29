import shutil
from pathlib import Path


CONFIG_DIR = Path.home() / ".config" / "YMD"
VENV_DIR = Path.home() / ".venvs" / "ymd"
BIN_DIR = Path.home() / ".local" / "bin"
LAUNCHER = BIN_DIR / "ymd"


def main() -> None:
    print("Uninstalling YMD...")

    if LAUNCHER.is_symlink() or LAUNCHER.is_file():
        LAUNCHER.unlink()
        print("Command removed.")
    else:
        print("Command not found.")

    if VENV_DIR.exists():
        shutil.rmtree(VENV_DIR)
        print("Virtual environment removed.")
    else:
        print("Virtual environment not found.")

    if CONFIG_DIR.exists():
        shutil.rmtree(CONFIG_DIR)
        print("Configuration removed.")

    print("YMD uninstalled successfully.")


if __name__ == "__main__":
    main()
