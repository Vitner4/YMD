import json
from pathlib import Path
from platformdirs import user_config_path


class Paths:
    def __init__(self):
        self.config_file = user_config_path("YMD") / "config.json"

    def save(self, path: str) -> Path:
        path = Path(path).expanduser().resolve()

        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        self.config_file.write_text(
            json.dumps({"output_path": str(path)},
                       ensure_ascii=False),
            encoding="utf-8",
        )

        return path

    def load(self) -> Path:
        if self.config_file.exists():
            data = json.loads(
                self.config_file.read_text(encoding="utf-8")
            )
            return Path(data["output_path"])

        return Path.home() / "Music"

    def get_path(self):
        data = json.loads(self.config_file.read_text(encoding="utf-8"))
        return data["output_path"]

    def get_config_path(self):
        return str(self.config_file)