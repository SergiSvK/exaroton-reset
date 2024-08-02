# 🚀 Exaroton Server Scheduler

This project is a Python application that schedules and manages the start of an Exaroton server at a specific time each day. It uses Docker for containerization and GitHub Actions for continuous integration and deployment.

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Fork](https://img.shields.io/github/forks/sergisvk/exaroton-reset?style=social)](https://github.com/sergisvk/exaroton-reset/fork)

## 📋 Requirements

- Python 3.10 🐍
- Docker 🐳
- GitHub Actions ⚙️
- An Exaroton account 🌐

## 🛠️ Installation

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
    ```

### Explanation of each environment variable

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

#### Examples of cron expressions:

- `0 6 * * *`: Runs the task at 6:00 AM every day.
- `*/15 * * * *`: Runs the task every 15 minutes.
- `0 0 1 * *`: Runs the task at midnight on the first day of every month.
- `0 12 * * 1-5`: Runs the task at 12:00 PM (noon) from Monday to Friday.

1. Build the Docker image and run the container:
    ```sh
    docker build -t exaroton-reset .
    docker run --env-file .env exaroton-reset
    ```

## 🚀 Uso

The application will run and schedule the start of the Exaroton server at the specified time in the configured time zone. It will also send notifications via a webhook.
## 🚢 Deployment

The project is configured to deploy automatically using GitHub Actions. Whenever a new version is released or a push is made to the `master` branch, a new Docker image will be built and published to the GitHub Container Registry.

### Deployment with Docker Compose

To deploy the project using Docker Compose, follow these steps:

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
        restart: unless-stopped
    ```

2. Run the following command to start the container:

    ```sh
    docker-compose up -d
    ```

This will start the container using the latest image published in the GitHub Container Registry and the environment variables defined in the `.env` file.

## 📂 Important Files

- `main.py`: Contains the main logic of the application.
- `Dockerfile`: Defines how the Docker image is built.
- `requirements.txt`: List of Python dependencies.
- `.github/workflows/docker-image.yml`: GitHub Actions configuration for CI/CD.
- `.env`: Environment variable configuration file (not included in the repository).

## 🤝 Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes you would like to make.

## 📄 License

This project is licensed under the MIT Licence. See the `LICENSE` file for more details.
