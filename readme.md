<div align="center">
  <h1>
    🚀 Exaroton Server Scheduler
    <br/>
    <br/>
    <p align="center">
      <img src="docs/readme-banner.png" alt="Banner Exaroton">
   </p>
  </h1>

   [![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
   [![Docker Image Build](https://github.com/SergiSvK/exaroton-reset/actions/workflows/docker-image.yml/badge.svg)](https://github.com/SergiSvK/exaroton-reset/actions/workflows/docker-image.yml)
   [![Github Commits](https://img.shields.io/github/last-commit/sergisvk/exaroton-reset)](https://github.com/sergisvk/exaroton-reset)
   [![Spanish](https://raw.githubusercontent.com/pedromxavier/flag-badges/main/badges/ES.svg)](docs/readme-es.md)
   [![GitHub License](https://img.shields.io/github/license/SergiSvK/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/blob/main/LICENSE)
</div>

<p align="center">
  The application will run and schedule the start of the Exaroton server at the specified time in the configured time zone.
  And it will send a notification to the specified webhook URL when the server is started.
</p>


## 📋 Requirements

> [!IMPORTANT]  
> - Python 3.10 to latest 🐍
> - An Exaroton account 🌐
> - Docker 🐳 (optional)

## 📑 Table of Contents

- [🚀 Exaroton Server Scheduler](#-exaroton-server-scheduler)
- [📋 Requirements](#-requirements)
- [⭐ Direct Script Execution](#-direct-script-execution)
- [🐳 Docker Execution](#-docker-execution)
  - [Option 1: Docker Execution](#option-1-docker-execution)
  - [Option 2: Docker Compose Execution](#option-2-docker-compose-execution)
- [🌱 Explanation of Environment Variables](#-explanation-of-environment-variables)
- [🤝 Contributions](#-contributions)
- [📄 License](#-license)

##  ⭐ Direct Script Execution

1. Clone the repository:
    ```sh
    git clone https://github.com/sergisvk/exaroton-reset.git
    cd exaroton-reset
    ```

2. Create a `.env` file in the root directory of the project and add the following environment variables:
> [!NOTE]
> [Click here](#-explanation-of-environment-variables) to see the explanation of each environment variable.

    ```env
    TOKEN=
    TIMEZONE=Europe/Madrid
    WEBHOOK_URL=
    CRON_SCHEDULE="0 6 * * *"
    ID_SERVER=""
    LANGUAGE="es-ES"
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the script:
    ```sh
    python main.py
    ```

## 🐋 Docker Execution

### Option 1: Docker Execution

1. Clone the repository:
    ```sh
    git clone https://github.com/sergisvk/exaroton-reset.git
    cd exaroton-reset
    ```

2. Create a `.env` file in the root directory of the project and add the following environment variables:

    ```env
    TOKEN=
    TIMEZONE=Europe/Madrid
    WEBHOOK_URL=
    CRON_SCHEDULE="0 6 * * *"
    ID_SERVER=""
    LANGUAGE="es-ES"
    ```

3. Build the Docker image and run the container:
    ```sh
    docker build -t exaroton-reset .
    docker run --env-file .env exaroton-reset
    ```
   
### Option 2: Docker Compose Execution

> [!TIP]
> In my opinion, this is the best way to run the container using Docker Compose.

1. Create a `docker-compose.yml` file in the root directory of the project with the following content:

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
          - CRON_SCHEDULE=${CRON_SCHEDULE}
          - LANGUAGE=${LANGUAGE}
        restart: unless-stopped
    ```


2. Run the following command to start the container:
   Another way to run the container using Docker Compose is
   to pass the `.env` file in the `environment` section of the `docker-compose.yml` file.

    ```yaml
    version: '3.8'

    services:
      exaroton-reset:
        image: ghcr.io/sergisvk/exaroton-reset:latest
        env_file:
          - .env
        restart: unless-stopped
    ```

This will start the container using the latest image published in the GitHub Container Registry and the environment variables defined in the `.env` file.


## 🌱 Explanation of Environment Variables

- `TOKEN`: This is the Exaroton API token used to authenticate requests to the Exaroton API. You must get this token from your Exaroton account.

- `TIMEZONE`: The time zone in which you want to schedule the server start. It must be in a recognized [tz](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) format (e.g., `Europe/Madrid`).

- `WEBHOOK_URL`: The webhook URL where notifications will be sent. This can be a Discord webhook URL or another service that accepts webhooks.

- `CRON_SCHEDULE`: The cron schedule for starting the server. In this case, it is set to start the server every day at 6:00 AM (`"0 6 * * *"`).

- `ID_SERVER`: The ID of your Exaroton server. This ID is unique for each server and is used to identify the server you want to start.

### Explanation of cron functionality

The cron format is used to schedule tasks at specific intervals. The syntax of a cron expression is as follows:

```cmd
* * * * *
| | | | |
| | | | +---- Day of the week (0 - 7) (Sunday to Saturday, where 0 and 7 are Sunday)
| | | +------ Month (1 - 12)
| | +-------- Day of the month (1 - 31)
| +---------- Hour (0 - 23)
+------------ Minute (0 - 59)
```

Each field can contain one or more values, separated by commas. Values can be specific numbers, ranges of numbers, or special characters such as `*` (any value), `/` (increments), and `-` (ranges).

## 🤝 Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes you would like to make.

## 📄 License

This project is licensed under the MIT Licence. See the `LICENSE` file for more details.