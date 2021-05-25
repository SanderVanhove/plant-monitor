import os
from os import mkdir, listdir, path
from os.path import isdir, isfile
import json
from dataclasses import asdict
from shutil import copyfile
from datetime import datetime

from sensors import SensorReading
from config import Config

GIT_DIR = "data-repo"


def commit_data(metric_values: SensorReading, pic_path: str, config: Config):
    # Make sure the repo is cloned
    if not isdir(GIT_DIR):
        mkdir(GIT_DIR)
        os.system(f"git clone {config.data_repo} {GIT_DIR}")


    # Add the current values and picture
    values_path = path.join(GIT_DIR, "values.json")
    old_values = {}
    if isfile(values_path):
        with open(values_path, "r") as values_file:
            old_values = json.load(values_file)

    values_dict = asdict(metric_values)
    values_dict["date"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
    if pic_path:
        os.system(f"cd {GIT_DIR};git reset --hard {config.reset_commit};git reflog expire --expire=now --all;git repack -ad;git prune")
        values_dict["image_date"] = values_dict["date"]
    elif "image_data" in old_values:
        values_dict["image_date"] = old_values["image_date"]

    with open(values_path, "w") as values_file:
        json.dump(values_dict, values_file)

    if pic_path:
        git_pic_path = path.join(GIT_DIR, "pic.jpg")
        copyfile(pic_path, git_pic_path)

    # Commit and push
    os.system(f"cd {GIT_DIR};git add *;git commit -m 'Update values and picture';git push -f")
