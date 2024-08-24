import datetime
import os
import time
import json
import pytz
from exaroton import Exaroton
from croniter import croniter
from weebhook_send import WebhookSend

# Variables de entorno
exa = Exaroton(os.getenv("TOKEN"))
id_server = os.getenv("ID_SERVER")
timezone = pytz.timezone(os.getenv("TIMEZONE"))
cron_schedule = os.getenv("CRON_SCHEDULE")
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


def schedule_cron_task():
    """
    Schedules a task to start the server based on the cron schedule.
    It calculates the next run time, waits until that time, and then starts the server.
    This process repeats indefinitely.

    Returns:
    - None
    """
    try:
        now_utc = datetime.datetime.now(pytz.utc)
        cron = croniter(cron_schedule, now_utc)
        next_run_time = cron.get_next(datetime.datetime)
        next_run_time = next_run_time.astimezone(timezone)

        delay_seconds = (next_run_time - now_utc).total_seconds()
        delay_hours = delay_seconds / 3600

        WebhookSend.send_message(translations['scheduled_start'].format(time=next_run_time.strftime("%H:%M"),
                                                                        timezone=timezone, hours=f"{delay_hours:.2f}"))

        time.sleep(delay_seconds)
        start_server()

        while True:
            next_run_time = cron.get_next(datetime.datetime)
            next_run_time = next_run_time.astimezone(timezone)
            delay_seconds = (next_run_time - datetime.datetime.now(pytz.utc)).total_seconds()
            time.sleep(delay_seconds)
            start_server()
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
