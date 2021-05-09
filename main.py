from time import sleep

from camera import capture_picture
from sensors import get_metrics
from webscript import post_message
from config import load_config
from display import register_display, show_error, update_info
from git import commit_data


def main():
    config = load_config()

    register_display()

    while True:
        # Get Values
        metric_values = get_metrics()
        update_info(metric_values)
        print("Measured some values:", metric_values)

        # Take a pic
        pic_path = capture_picture(config)
        print("Snapped a pic:", pic_path)

        # Post values to Waylay
        post_success = post_message(metric_values, config)

        # Commit to git data repo
        commit_data(metric_values, pic_path, config)

        print()

        sleep(config.measure_interval)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        show_error(type(e).__name__)

        raise e