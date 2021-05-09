from picamera import PiCamera
from datetime import datetime
from os import path, mkdir
from os.path import isdir


def capture_picture(pic_dir: str = "pics/") -> str:
    """ 
    Snap a picture and return its path.
    """
    if not isdir(pic_dir):
        mkdir(pic_dir)

    camera = PiCamera()

    try:
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.jpg")
        pic_path = path.join(pic_dir, date)

        camera.capture(pic_path)

        return pic_path
    finally:
        camera.close()
