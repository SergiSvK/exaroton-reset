import datetime
import os
import time

import pytz
from exaroton import Exaroton
from croniter import croniter
from weebhook_send import WebhookSend

# Variables de entorno
exa = Exaroton(os.getenv("TOKEN"))
id_server = os.getenv("ID_SERVER")
timezone = pytz.timezone(os.getenv("TIMEZONE"))
cron_schedule = os.getenv("CRON_SCHEDULE")


def start_server():
    """
    Starts the server using the Exaroton client and sends a notification via webhook.

    Returns:
    - None
    """
    try:
        print(exa.start(id_server))
        WebhookSend.send_message("💚 Servidor iniciado correctamente")
        print("Server iniciado")
    except Exception as er:
        WebhookSend.send_message(f"❌ Error al iniciar el servidor: {er}")
        print(f"Error al iniciar el servidor: {er}")


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

        WebhookSend.send_message(f"⏰ Programado para iniciar el servidor a las "
                                 f"{next_run_time.strftime('%H:%M')} UTC ({timezone.zone}). "
                                 f"Faltan {delay_hours:.2f} horas")

        time.sleep(delay_seconds)
        start_server()

        while True:
            next_run_time = cron.get_next(datetime.datetime)
            next_run_time = next_run_time.astimezone(timezone)
            delay_seconds = (next_run_time - datetime.datetime.now(pytz.utc)).total_seconds()
            time.sleep(delay_seconds)
            start_server()
    except Exception as er:
        WebhookSend.send_message(f"❌ Error en la programación de la tarea cron: {er}")
        print(f"Error en la programación de la tarea cron: {er}")


if __name__ == '__main__':
    """
    Main entry point of the script. Prints account and server information, then schedules the cron task.
    Read -> readme.md for more information.

    Returns:
    - None
    """
    try:
        print("==" * 50)
        print(exa.get_account())
        print("==" * 50)
        print(exa.get_server(id_server))
        print("==" * 50)

        schedule_cron_task()
    except Exception as e:
        WebhookSend.send_message(f"❌ Error en el script principal: {e}")
        print(f"Error en el script principal: {e}")
