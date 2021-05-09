from picamera import PiCamera
from datetime import datetime
from time import sleep
from os import path, mkdir

PIC_FOLDER = "./pics/"
PIC_DELAY = 10 * 60 # 10 minutes

if not path.exists(PIC_FOLDER):
    mkdir(PIC_FOLDER)

camera = PiCamera()

for _ in range(6):
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S.jpg")
    pic_path = path.join(PIC_FOLDER, date)

    camera.capture(pic_path)

    sleep(PIC_DELAY)