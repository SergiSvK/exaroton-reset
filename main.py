import datetime
import os
import time

import pytz
from exaroton import Exaroton

from weebhook_send import WebhookSend

# Tu clave de API para exaroton
exa = Exaroton(os.getenv("TOKEN"))

# ID del servidor
id_server = "Y3yZFLfiTYSwOl6d"

# Definir la zona horaria de Chile
timezone = pytz.timezone(os.getenv("TIMEZONE"))


def start_server():
    print(exa.start(id_server))
    WebhookSend.send_message("💚 Servidor iniciado correctamente")
    print("Server iniciado")


# Función que programa la tarea diaria
def schedule_daily_task():
    now_utc = datetime.datetime.now(pytz.utc)
    now_timezone = now_utc.astimezone(timezone)
    next_run_time = now_timezone.replace(hour=int(os.getenv("HOUR")), minute=int(os.getenv("MINUTE")), second=0,
                                         microsecond=0)

    if now_timezone >= next_run_time:
        next_run_time += datetime.timedelta(days=1)

    schedule_time = next_run_time.astimezone(pytz.utc)

    delay_seconds = (schedule_time - now_utc).total_seconds()
    delay_hours = delay_seconds / 3600

    WebhookSend.send_message(f":radio_button: Programado para iniciar el servidor a las "
                             f"{next_run_time.strftime('%H:%M')} UTC ({timezone.zone}). Faltan {delay_hours:.2f} horas")

    time.sleep(delay_seconds)
    start_server()

    while True:
        time.sleep(24 * 3600)
        start_server()


if __name__ == '__main__':
    print("==" * 50)
    print(exa.get_account())
    print("==" * 50)
    print(exa.get_server(id_server))
    print("==" * 50)

    schedule_daily_task()
