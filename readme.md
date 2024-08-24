<div align="center">
  <h1>
    🚀 Exaroton Server Scheduler
    <br/>
    <br/>
    <p align="center">
      <img src="docs/readme-banner.png" alt="Banner Exaroton">
   </p>
  </h1>

  [![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
  [![Docker Image Build](https://github.com/SergiSvK/exaroton-reset/actions/workflows/docker-image.yml/badge.svg)](https://github.com/SergiSvK/exaroton-reset/actions/workflows/docker-image.yml)
  [![Github Commits](https://img.shields.io/github/last-commit/sergisvk/exaroton-reset)](https://github.com/sergisvk/exaroton-reset)
  [![GitHub License](https://img.shields.io/github/license/SergiSvK/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/blob/main/LICENSE)
  ![Discord](https://img.shields.io/discord/301997437156065281?style=plastic&logo=discord&label=contact)

  <h2>Choose Your Language</h2>
  <table align="center">
    <tr>
      <td align="center">
        <a href="docs/readme-es.md">
          <img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg" alt="Español" width="50" height="50"/>
          <br/>
          <button>Español</button>
        </a>
      </td>
    </tr>
  </table>
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

    ```env
    TOKEN=
    TIMEZONE=Europe/Madrid
    WEBHOOK_URL=
    CRON_SCHEDULE_START="0 6 * * *" # Start the server at 6:00 AM
    CRON_SCHEDULE_STOP="0 22 * * *" # Stop the server at 10:00 PM
    ID_SERVER=""
    LANGUAGE=""
    ```
   > [!NOTE]
   > [Click here](#-explanation-of-environment-variables) to see the explanation of each environment variable.

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
    CRON_SCHEDULE_START="0 6 * * *" # Start the server at 6:00 AM
    CRON_SCHEDULE_STOP="0 22 * * *" # Stop the server at 10:00 PM
    ID_SERVER=""
    LANGUAGE="es-ES"
    ```
   > [!NOTE]
   > [Click here](#-explanation-of-environment-variables) to see the explanation of each environment variable.

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
          - CRON_SCHEDULE_START=${CRON_SCHEDULE_START}
          - CRON_SCHEDULE_STOP=${CRON_SCHEDULE_STOP}
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

- `CRON_SCHEDULE_START`: The cron schedule for starting the server. In this case, it is set to start the server every day at 6:00 AM (`"0 6 * * *"`).

- `CRON_SCHEDULE_STOP`: The cron schedule for stopping the server. In this case, it is set to stop the server every day at 10:00 PM (`"0 22 * * *"`).

- `ID_SERVER`: The ID of your Exaroton server. This ID is unique for each server and is used to identify the server you want to start.

- `LANGUAGE`: The language in which the notifications will be sent. 
   The available languages are `en-UK`, `es-ES`,`fr-FR`, `pt-PT`

### Explanation of CRON functionality

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

[![GitHub Contributors](https://img.shields.io/github/contributors/sergisvk/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/pulls)
[![GitHub Issues](https://img.shields.io/github/issues/sergisvk/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/issues)

## 🪙 Donate

This project is maintained by SergiSvK. If you find this project helpful, please consider making a donation.

<div align="center">
  <table align="center">
    <tr>
      <td align="center">
        <a href="https://btcscan.org/address/3AWqbrfMp1Z36XPGNmuZQAmxWZmKDqKGjW" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg" alt="BTC Logo" width="50" height="50"/>
          <br/>
          <button>Donate BTC</button>
        </a>
      </td>
      <td align="center">
        <a href="https://etherscan.io/address/0x1D31ccEa10207FF603b0b837Ed8Fb47454aeeff6" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Ethereum-icon-purple.svg" alt="ETH Logo" width="50" height="50"/>
          <br/>
          <button>Donate ETH</button>
        </a>
      </td>
    </tr>
  </table>
</div>


## 📄 License

This project is licensed under the MIT Licence. See the [LICENSE](LICENSE) file for more information.