from picamera import PiCamera
from datetime import datetime
from os import path, mkdir
from os.path import isdir

from config import Config


def capture_picture(config: Config) -> str:
    """ 
    Snap a picture and return its path.
    """
    pic_dir = config.pic_dir
    if not isdir(pic_dir):
        mkdir(pic_dir)

    camera = PiCamera()
    camera.resolution = config.pic_resolution

    try:
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.jpg")
        pic_path = path.join(pic_dir, date)

        camera.capture(pic_path)

        return pic_path
    finally:
        camera.close()
