from requests import post
import json
from dataclasses import asdict
import warnings
from os import path

from sensors import SensorReading
from config import Config


def post_message(data: SensorReading, config: Config) -> bool:
    json_data = asdict(data)
    url = path.join(config.data_url, config.resource_id)
    auth = (config.api_key, config.api_secret)

    request = post(url, json=json_data, auth=auth)

    if not request.ok:
        warnings.warn(request.content)
        return False
    
    return True
