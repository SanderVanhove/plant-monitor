from time import sleep
from datetime import datetime

from grove.factory import Factory
from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton

from sensors import get_metrics, SensorReading


def register_display():
    lcd = Factory.getDisplay("JHD1802")
    ledbtn = GroveLedButton(5)

    lcd.backlight(False)
    lcd.clear()


    def on_button_click(index, event, time):
        if not event & Button.EV_SINGLE_CLICK:
            return

        lcd.backlight(True)

        metric_values = get_metrics()
        update_info(metric_values)


        sleep(5)

        lcd.backlight(False)

    ledbtn.on_event = on_button_click


def update_info(metric_values: SensorReading):
    lcd = Factory.getDisplay("JHD1802")

    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.write(f"T: {metric_values.temperature} H: {metric_values.humidity} {datetime.now().minute}")

    lcd.setCursor(1, 0)
    lcd.write(f"M: {metric_values.moisture} L: {metric_values.light}")


def show_error(error: str):
    lcd = Factory.getDisplay("JHD1802")

    lcd.backlight(True)
    lcd.setCursor(0, 0)
    lcd.write("I died :(")

    lcd.setCursor(1, 0)
    lcd.write(error)
