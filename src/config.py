import json
import os

CONFIG_FILE = "config.json"


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), CONFIG_FILE)
    with open(config_path) as f:
        return json.load(f)


config = load_config()
