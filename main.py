from time import sleep

from camera import capture_picture
from sensors import get_metrics
from webscript import post_message
from config import load_config
from display import register_display, show_error, update_info


def main():
    config = load_config()

    register_display()

    while True:

        print("I'm waking up :D")

        # Get Values
        metric_values = get_metrics()
        update_info(metric_values)
        print("Measured some values:", metric_values)

        # Take a pic
        pic_path = capture_picture(config.pic_dir)
        print("Snapped a pic:", pic_path)

        # Post values to Waylay
        post_success = post_message(metric_values, config)

        if post_success:
            print("Values posted.")
        else:
            print("Something went wrong :/")

        print()

        sleep(config.measure_interval)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        show_error(type(e).__name__)

        raise e