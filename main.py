import datetime
import os
import time
import json
import pytz
from exaroton import Exaroton
from croniter import croniter
from weebhook_send import WebhookSend


def check_and_install_requirements():
    """
    Checks if the required libraries are installed and installs them if they are not.

    Returns:
    - None
    """
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    for lib in requirements:
        try:
            __import__(lib)
            print(f'{lib} is already installed')
        except ImportError:
            os.system(f'pip install {lib}')
            print(f'{lib} has been installed')


check_and_install_requirements()

# Load environment variables
exa = Exaroton(os.getenv("TOKEN"))
id_server = os.getenv("ID_SERVER")
timezone = pytz.timezone(os.getenv("TIMEZONE"))
cron_schedule_start = os.getenv("CRON_SCHEDULE_START")
cron_schedule_stop = os.getenv("CRON_SCHEDULE_STOP")
language = os.getenv("LANGUAGE")


def load_translations(lang: str) -> dict:
    """
    Loads the translations from the language file.

    Args:
    - language (str): The language code to load the translations from.

    Returns:
    - dict: The translations are loaded from the language file.
    """
    if not os.path.exists(f'lang/{lang}.json'):
        raise FileNotFoundError(f'Language file not found: {lang}')

    with open(f'lang/{lang}.json', 'r', encoding='utf-8') as file:
        return json.load(file)


translations = load_translations(language)


def start_server():
    """
    Starts the server using the Exaroton client and sends a notification via webhook.

    Returns:
    - None
    """
    try:
        print(exa.start(id_server))
        WebhookSend.send_message(translations['server_started'])
        print(translations['server_started'])
    except Exception as er:
        WebhookSend.send_message(translations['server_start_error'].format(error=er))
        print(translations['server_start_error'].format(error=er))


def stop_server():
    """
    Stops the server using the Exaroton client and sends a notification via webhook.

    Returns:
    - None
    """
    try:
        print(exa.stop(id_server))
        WebhookSend.send_message(translations['server_stopped'])
        print(translations['server_stopped'])
    except Exception as er:
        WebhookSend.send_message(translations['server_stop_error'].format(error=er))
        print(translations['server_stop_error'].format(error=er))


def wait_until_next_cron(cron_schedule: str, timezone: pytz.timezone, action: str):
    """
    Calculates the next scheduled time for the given cron and waits until that time.

    Args:
    - cron_schedule (str): The cron schedule string.
    - timezone (pytz.timezone): The timezone to calculate the time in.
    - action (str): Describes the action to be performed (start or stop) for logging.

    Returns:
    - None
    """
    now_utc = datetime.datetime.now(pytz.utc)
    cron = croniter(cron_schedule, now_utc)
    next_run_time = cron.get_next(datetime.datetime)
    next_run_time = next_run_time.astimezone(timezone)

    delay_seconds = (next_run_time - now_utc).total_seconds()
    delay_hours = delay_seconds / 3600

    WebhookSend.send_message(translations[f'scheduled_{action}'].format(time=next_run_time.strftime("%H:%M"),
                                                                        timezone=timezone, hours=f"{delay_hours:.2f}"))

    time.sleep(delay_seconds)


def schedule_cron_task():
    """
    Schedules tasks to start and stop the server based on the cron schedules.
    It calculates the next run time for both start and stop, waits until those times,
    and then executes the corresponding action.
    This process repeats indefinitely.

    Returns:
    - None
    """
    try:
        while True:
            # Wait until the next start time and start the server
            wait_until_next_cron(cron_schedule_start, timezone, 'start')
            start_server()

            # Wait until the next stop time and stop the server
            wait_until_next_cron(cron_schedule_stop, timezone, 'stop')
            stop_server()
    except Exception as er:
        WebhookSend.send_message(translations['cron_task_error'].format(error=er))
        print(translations['cron_task_error'].format(error=er))


if __name__ == '__main__':
    """
    Main entry point of the script. Prints account and server information, then schedules the cron task.
    Read -> readme.md for more information.
    """

    try:
        print("==" * 50)
        print(translations['account_info'])
        print(exa.get_account())
        print("==" * 50)
        print(translations['server_info'])
        print(exa.get_server(id_server))
        print("==" * 50)

        schedule_cron_task()
    except Exception as e:
        WebhookSend.send_message(translations['main_script_error'].format(error=e))
        print(translations['main_script_error'].format(error=e))
