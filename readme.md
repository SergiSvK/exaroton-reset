# 🚀 Exaroton Server Scheduler
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Fork](https://img.shields.io/github/forks/sergisvk/exaroton-reset?style=social)](https://github.com/sergisvk/exaroton-reset/fork)

Select another language:

[![Spanish](https://img.shields.io/badge/lang-es-red.svg)](docs/readme-es.md)

The application will run and schedule the start of the Exaroton server at the specified time in the configured time zone. 
T will also send notifications via a webhook.

There are **two options** to run the application: Directly executing the script or using Docker. 
After choosing one of the options, follow the steps below to install the application.
Please note that you need to have an Exaroton account and an API token to use this application.

## 📋 Requirements

> [!IMPORTANT]  
> - Python 3.10 to latest 🐍
> - An Exaroton account 🌐
> - Docker 🐳 (optional)

## 📑 Table of Contents





##  ⭐ Direct Script Execution

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

The project is configured to deploy automatically using GitHub Actions. 
Whenever a new version is released or a push is made to the `master` branch, 
a new Docker image will be built and published to the GitHub Container Registry.

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