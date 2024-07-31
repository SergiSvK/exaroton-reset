# 🚀 Exaroton Server Scheduler

Este proyecto es una aplicación en Python que programa y gestiona el inicio de un servidor de Exaroton a una hora específica cada día. Utiliza Docker para la contenedorización y GitHub Actions para la integración y despliegue continuo.

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Fork](https://img.shields.io/github/forks/sergisvk/exaroton-reset?style=social)](https://github.com/sergisvk/exaroton-reset/fork)

## 📋 Requisitos

- Python 3.10 🐍
- Docker 🐳
- GitHub Actions ⚙️
- Una cuenta en Exaroton 🌐

## 🛠️ Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/sergisvk/exaroton-reset.git
    cd exaroton-reset
    ```

2. Crea un archivo `.env` en el directorio raíz del proyecto y añade las siguientes variables de entorno:

    ```env
    TOKEN=
    TIMEZONE=Europe/Madrid
    WEBHOOK_URL=
    CRON_SCHEDULE="0 6 * * *"
    ID_SERVER=""
    ```

### Explicación de cada variable de entorno

- `TOKEN`: Este es el token de API de Exaroton que se utiliza para autenticar las solicitudes a la API de Exaroton. Debes obtener este token desde tu cuenta de Exaroton. Simply get an API Token from your Account and you're good to go.

- `TIMEZONE`: La zona horaria en la que deseas programar el inicio del servidor. Debe estar en un formato reconocido [tz](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por ejemplo, `Europe/Madrid`).

- `WEBHOOK_URL`: La URL del webhook donde se enviarán las notificaciones. Esto puede ser una URL de webhook de Discord u otro servicio que acepte webhooks.

- `CRON_SCHEDULE`: La programación cron para iniciar el servidor. En este caso, está configurado para iniciar el servidor todos los días a las 6:00 AM (`"0 6 * * *"`).

- `ID_SERVER`: El ID de tu servidor de Exaroton. Este ID es único para cada servidor y se utiliza para identificar el servidor que deseas iniciar.

### Explicación del funcionamiento del cron

El formato de cron se utiliza para programar tareas en intervalos específicos. La sintaxis de una expresión cron es la siguiente:

```cmd
* * * * *
| | | | |
| | | | +---- Día de la semana (0 - 7) (domingo a sábado, donde 0 y 7 son domingo)
| | | +------ Mes (1 - 12)
| | +-------- Día del mes (1 - 31)
| +---------- Hora (0 - 23)
+------------ Minuto (0 - 59)
```

Cada campo puede contener uno o más valores, separados por comas. Los valores pueden ser números específicos, rangos de números, o caracteres especiales como `*` (cualquier valor), `/` (incrementos), y `-` (rangos).

#### Ejemplos de expresiones cron:

- `0 6 * * *`: Ejecuta la tarea todos los días a las 6:00 AM.
- `*/15 * * * *`: Ejecuta la tarea cada 15 minutos.
- `0 0 1 * *`: Ejecuta la tarea a la medianoche del primer día de cada mes.
- `0 12 * * 1-5`: Ejecuta la tarea a las 12:00 PM de lunes a viernes.

1. Construye y ejecuta el contenedor Docker:
    ```sh
    docker build -t exaroton-reset .
    docker run --env-file .env exaroton-reset
    ```

## 🚀 Uso

La aplicación se ejecutará y programará el inicio del servidor de Exaroton a la hora especificada en la zona horaria configurada. También enviará notificaciones a través de un webhook.

## 🚢 Despliegue

El proyecto está configurado para desplegarse automáticamente utilizando GitHub Actions. Cada vez que se publique una nueva versión o se haga un push a la rama `master`, se construirá y publicará una nueva imagen Docker en el GitHub Container Registry.

### Despliegue con Docker Compose

Para desplegar el proyecto utilizando Docker Compose, sigue estos pasos:

1. Crea un archivo `docker-compose.yml` en el directorio raíz del proyecto con el siguiente contenido:

    ```yaml
    version: '3.8'

    services:
      exaroton-reset:
        image: ghcr.io/sergisvk/exaroton-reset:latest
        environment:
          - TOKEN=${TOKEN}
          - HOUR=${HOUR}
          - MINUTE=${MINUTE}
          - TIMEZONE=${TIMEZONE}
          - WEBHOOK_URL=${WEBHOOK_URL}
        restart: unless-stopped
    ```

2. Ejecuta el siguiente comando para iniciar el contenedor:

    ```sh
    docker-compose up -d
    ```

Esto iniciará el contenedor utilizando la imagen más reciente publicada en el GitHub Container Registry y las variables de entorno definidas en el archivo `.env`.

## 📂 Archivos Importantes

- `main.py`: Contiene la lógica principal de la aplicación.
- `Dockerfile`: Define cómo se construye la imagen Docker.
- `requirements.txt`: Lista de dependencias de Python.
- `.github/workflows/docker-image.yml`: Configuración de GitHub Actions para CI/CD.
- `.env`: Archivo de configuración de variables de entorno (no incluido en el repositorio).

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
