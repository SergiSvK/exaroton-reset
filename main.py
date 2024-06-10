import datetime
import os
import time

import pytz
from exaroton import Exaroton

# Tu clave de API para exaroton
exa = Exaroton(os.getenv("TOKEN"))

# ID del servidor
id_server = "Y3yZFLfiTYSwOl6d"

# Definir la zona horaria de Chile
timezone_chile = pytz.timezone('Chile/Continental')


def start_server():
    print(exa.start(id_server))
    print("Server iniciado")


# Función que programa la tarea diaria
def schedule_daily_task():
    now_utc = datetime.datetime.now(pytz.utc)
    now_chile = now_utc.astimezone(timezone_chile)
    next_run_time = now_chile.replace(hour=6, minute=0, second=0, microsecond=0)

    if now_chile >= next_run_time:
        next_run_time += datetime.timedelta(days=1)

    schedule_time = next_run_time.astimezone(pytz.utc)

    delay_seconds = (schedule_time - now_utc).total_seconds()
    delay_hours = delay_seconds / 3600
    print(f"Programado para iniciar el servidor a las 6:00 AM en Chile, en {delay_hours:.2f} horas.")

    time.sleep(delay_seconds)
    start_server()

    while True:
        time.sleep(24 * 3600)  # Dormir 24 horas
        start_server()


if __name__ == '__main__':
    print("==" * 50)
    print(exa.get_account())
    print("==" * 50)
    print(exa.get_server(id_server))
    print("==" * 50)

    schedule_daily_task()
