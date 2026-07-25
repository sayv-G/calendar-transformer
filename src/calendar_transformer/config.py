from pathlib import Path

import yaml


def load_yaml(filename):
    """
    Lädt eine YAML-Datei aus dem config-Ordner.
    """

    path = Path("config") / filename

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)