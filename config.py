from dataclasses import dataclass
from os.path import isfile
import json


@dataclass
class Config:
    pic_dir: str
    pic_resolution: str
    measure_interval: float
    webscript_url: str
    data_repo: str
    reset_commit: str


def load_config() -> Config:
    assert isfile("config.json"), "Please create a `config.json` based on `config-example.json`."

    with open("config.json") as config_file:
        config = json.load(config_file)

        return Config(
            config["pic_dir"],
            config["pic_resolution"],
            config["measure_interval"],
            config["webscript_url"],
            config["data_repo"],
            config["reset_commit"],
        )
