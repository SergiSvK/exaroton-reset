<div align="center">
  <h1>
    🚀 Controlador de Servidor Exaroton
    <br/>
    <br/>
    <p align="center">
      <img src="readme-banner.png" alt="Banner Exaroton">
   </p>
  </h1>

   [![Versión de Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
   [![Construcción de Imagen Docker](https://github.com/SergiSvK/exaroton-reset/actions/workflows/docker-image.yml/badge.svg)](https://github.com/SergiSvK/exaroton-reset/actions/workflows/docker-image.yml)
   [![Commits en Github](https://img.shields.io/github/last-commit/sergisvk/exaroton-reset)](https://github.com/sergisvk/exaroton-reset)
   [![Licencia en GitHub](https://img.shields.io/github/license/SergiSvK/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/blob/main/LICENSE)
   [![Español](https://raw.githubusercontent.com/pedromxavier/flag-badges/main/badges/ES.svg)](docs/readme-es.md)
   ![Discord](https://img.shields.io/discord/301997437156065281?style=plastic&logo=discord&label=contact)

</div>

<p align="center">
  La aplicación se ejecutará y programará el inicio del servidor Exaroton a la hora especificada en la zona horaria configurada.
  Además, enviará una notificación a la URL del webhook especificado cuando el servidor se inicie.
</p>


## 📋 Requisitos

> [!IMPORTANTE]  
> - Python 3.10 o más reciente 🐍
> - Una cuenta de Exaroton 🌐
> - Docker 🐳 (opcional)

## 📑 Tabla de Contenidos

- [🚀 Planificador de Servidor Exaroton](#-planificador-de-servidor-exaroton)
- [📋 Requisitos](#-requisitos)
- [⭐ Ejecución Directa del Script](#-ejecución-directa-del-script)
- [🐳 Ejecución con Docker](#-ejecución-con-docker)
  - [Opción 1: Ejecución con Docker](#opción-1-ejecución-con-docker)
  - [Opción 2: Ejecución con Docker Compose](#opción-2-ejecución-con-docker-compose)
- [🌱 Explicación de Variables de Entorno](#-explicación-de-variables-de-entorno)
- [🤝 Contribuciones](#-contribuciones)
- [📄 Licencia](#-licencia)

## ⭐ Ejecución Directa del Script

1. Clona el repositorio:
    ```sh
    git clone https://github.com/sergisvk/exaroton-reset.git
    cd exaroton-reset
    ```

2. Crea un archivo `.env` en el directorio raíz del proyecto y agrega las siguientes variables de entorno:

    ```env
    TOKEN=
    TIMEZONE=Europe/Madrid
    WEBHOOK_URL=
    CRON_SCHEDULE_START="0 6 * * *" # Inicia el servidor a las 6:00 AM
    CRON_SCHEDULE_STOP="0 22 * * *" # Detiene el servidor a las 10:00 PM
    ID_SERVER=""
    LANGUAGE=""
    ```
   > [!NOTA]
   > [Haz clic aquí](#-explicación-de-variables-de-entorno) para ver la explicación de cada variable de entorno.

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Ejecuta el script:
    ```sh
    python main.py
    ```

## 🐋 Ejecución con Docker

### Opción 1: Ejecución con Docker

1. Clona el repositorio:
    ```sh
    git clone https://github.com/sergisvk/exaroton-reset.git
    cd exaroton-reset
    ```

2. Crea un archivo `.env` en el directorio raíz del proyecto y agrega las siguientes variables de entorno:

    ```env
    TOKEN=
    TIMEZONE=Europe/Madrid
    WEBHOOK_URL=
    CRON_SCHEDULE_START="0 6 * * *" # Inicia el servidor a las 6:00 AM
    CRON_SCHEDULE_STOP="0 22 * * *" # Detiene el servidor a las 10:00 PM
    ID_SERVER=""
    LANGUAGE="es-ES"
    ```
   > [!NOTA]
   > [Haz clic aquí](#-explicación-de-variables-de-entorno) para ver la explicación de cada variable de entorno.

3. Construye la imagen de Docker y ejecuta el contenedor:
    ```sh
    docker build -t exaroton-reset .
    docker run --env-file .env exaroton-reset
    ```
   
### Opción 2: Ejecución con Docker Compose

> [!TIP]
> En mi opinión, esta es la mejor manera de ejecutar el contenedor usando Docker Compose.

1. Crea un archivo `docker-compose.yml` en el directorio raíz del proyecto con el siguiente contenido:

    ```yaml
    version: '3.8'

    services:
      exaroton-reset:
        image: ghcr.io/sergisvk/exaroton-reset:latest
        environment:
          - TOKEN=${TOKEN}
          - TIMEZONE=${TIMEZONE}
          - WEBHOOK_URL=${WEBHOOK_URL}
          - ID_SERVER=${ID_SERVER}
          - CRON_SCHEDULE_START=${CRON_SCHEDULE_START}
          - CRON_SCHEDULE_STOP=${CRON_SCHEDULE_STOP}
          - LANGUAGE=${LANGUAGE}
        restart: unless-stopped
    ```


2. Ejecuta el siguiente comando para iniciar el contenedor:
   Otra forma de ejecutar el contenedor usando Docker Compose es
   pasar el archivo `.env` en la sección `environment` del archivo `docker-compose.yml`.

    ```yaml
    version: '3.8'

    services:
      exaroton-reset:
        image: ghcr.io/sergisvk/exaroton-reset:latest
        env_file:
          - .env
        restart: unless-stopped
    ```

Esto iniciará el contenedor utilizando la última imagen publicada en el Registro de Contenedores de GitHub y las variables de entorno definidas en el archivo `.env`.

## 🌱 Explicación de Variables de Entorno

- `TOKEN`: Este es el token de la API de Exaroton que se utiliza para autenticar las solicitudes a la API de Exaroton. Debes obtener este token desde tu cuenta de Exaroton.

- `TIMEZONE`: La zona horaria en la que deseas programar el inicio del servidor. Debe estar en un formato [tz](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) reconocido (por ejemplo, `Europe/Madrid`).

- `WEBHOOK_URL`: La URL del webhook donde se enviarán las notificaciones. Esto puede ser una URL de webhook de Discord u otro servicio que acepte webhooks.

- `CRON_SCHEDULE_START`: El cronograma para iniciar el servidor. En este caso, está configurado para iniciar el servidor todos los días a las 6:00 AM (`"0 6 * * *"`).

- `CRON_SCHEDULE_STOP`: El cronograma para detener el servidor. En este caso, está configurado para detener el servidor todos los días a las 10:00 PM (`"0 22 * * *"`).

- `ID_SERVER`: El ID de tu servidor Exaroton. Este ID es único para cada servidor y se utiliza para identificar el servidor que deseas iniciar.

- `LANGUAGE`: El idioma en el que se enviarán las notificaciones.
   Los idiomas disponibles son `en-UK`, `es-ES`, `fr-FR`, `pt-PT`.

### Explicación de la Funcionalidad CRON

El formato cron se utiliza para programar tareas en intervalos específicos.
La sintaxis de una expresión cron es la siguiente:

```cmd
* * * * *
| | | | |
| | | | +---- Día de la semana (0 - 7) (Domingo a Sábado, donde 0 y 7 son Domingo)
| | | +------ Mes (1 - 12)
| | +-------- Día del mes (1 - 31)
| +---------- Hora (0 - 23)
+------------ Minuto (0 - 59)
```

Cada campo puede contener uno o más valores, separados por comas. 
Los valores pueden ser números específicos, rangos de números o caracteres especiales como `*` (cualquier valor), `/` (incrementos) y `-` (rangos).

## 🤝 Contribuciones

Las contribuciones son bienvenidas.
Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

[![Contribuyentes en GitHub](https://img.shields.io/github/contributors/sergisvk/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/pulls)
[![Issues en GitHub](https://img.shields.io/github/issues/sergisvk/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/issues)

## 🪙 Donaciones

Este proyecto es mantenido por SergiSvK. Si encuentras este proyecto útil, considera hacer una donación.

<div align="center">
  <table align="center">
    <tr>
      <td align="center">
        <a href="https://btcscan.org/address/3AWqbrfMp1Z36XPGNmuZQAmxWZmKDqKGjW" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg" alt="BTC Logo" width="50" height="50"/>
          <br/>
          <button>Donar BTC</button>
        </a>
      </td>
      <td align="center">
        <a href="https://etherscan.io/address/0x1D31ccEa10207FF603b0b837Ed8Fb47454aeeff6" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Ethereum-icon-purple.svg" alt="ETH Logo" width="50" height="50"/>
          <br/>
          <button>Donar ETH</button>
        </a>
      </td>
    </tr>
  </table>
</div>


## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más información.
