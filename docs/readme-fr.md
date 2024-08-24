<div align="center">
  <h1>
    🚀 Planificateur de Serveur Exaroton
    <br/>
    <br/>
    <p align="center">
      <img src="readme-banner.png" alt="Bannière Exaroton">
   </p>
  </h1>

   [![Version de Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
   [![Construction d'Image Docker](https://github.com/SergiSvK/exaroton-reset/actions/workflows/docker-image.yml/badge.svg)](https://github.com/SergiSvK/exaroton-reset/actions/workflows/docker-image.yml)
   [![Commits sur Github](https://img.shields.io/github/last-commit/sergisvk/exaroton-reset)](https://github.com/sergisvk/exaroton-reset)
   [![Licence sur GitHub](https://img.shields.io/github/license/SergiSvK/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/blob/main/LICENSE)
   [![Français](https://raw.githubusercontent.com/pedromxavier/flag-badges/main/badges/FR.svg)](docs/readme-fr.md)
   ![Discord](https://img.shields.io/discord/301997437156065281?style=plastic&logo=discord&label=contact)

</div>

<p align="center">
  L'application s'exécutera et programmera le démarrage du serveur Exaroton à l'heure spécifiée dans le fuseau horaire configuré.
  Elle enverra également une notification à l'URL du webhook spécifiée lorsque le serveur sera démarré.
</p>


## 📋 Exigences

> [!IMPORTANT]  
> - Python 3.10 ou version ultérieure 🐍
> - Un compte Exaroton 🌐
> - Docker 🐳 (optionnel)

## 📑 Table des Matières

- [🚀 Planificateur de Serveur Exaroton](#-planificateur-de-serveur-exaroton)
- [📋 Exigences](#-exigences)
- [⭐ Exécution Directe du Script](#-exécution-directe-du-script)
- [🐳 Exécution avec Docker](#-exécution-avec-docker)
  - [Option 1 : Exécution avec Docker](#option-1-exécution-avec-docker)
  - [Option 2 : Exécution avec Docker Compose](#option-2-exécution-avec-docker-compose)
- [🌱 Explication des Variables d'Environnement](#-explication-des-variables-denvironnement)
- [🤝 Contributions](#-contributions)
- [📄 Licence](#-licence)

## ⭐ Exécution Directe du Script

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/sergisvk/exaroton-reset.git
    cd exaroton-reset
    ```

2. Créez un fichier `.env` dans le répertoire racine du projet et ajoutez les variables d'environnement suivantes :

    ```env
    TOKEN=
    TIMEZONE=Europe/Paris
    WEBHOOK_URL=
    CRON_SCHEDULE_START="0 6 * * *" # Démarre le serveur à 6h00
    CRON_SCHEDULE_STOP="0 22 * * *" # Arrête le serveur à 22h00
    ID_SERVER=""
    LANGUAGE=""
    ```
   > [!NOTE]
   > [Cliquez ici](#-explication-des-variables-denvironnement) pour voir l'explication de chaque variable d'environnement.

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

4. Exécutez le script :
    ```sh
    python main.py
    ```

## 🐋 Exécution avec Docker

### Option 1 : Exécution avec Docker

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/sergisvk/exaroton-reset.git
    cd exaroton-reset
    ```

2. Créez un fichier `.env` dans le répertoire racine du projet et ajoutez les variables d'environnement suivantes :

    ```env
    TOKEN=
    TIMEZONE=Europe/Paris
    WEBHOOK_URL=
    CRON_SCHEDULE_START="0 6 * * *" # Démarre le serveur à 6h00
    CRON_SCHEDULE_STOP="0 22 * * *" # Arrête le serveur à 22h00
    ID_SERVER=""
    LANGUAGE="fr-FR"
    ```
   > [!NOTE]
   > [Cliquez ici](#-explication-des-variables-denvironnement) pour voir l'explication de chaque variable d'environnement.

3. Construisez l'image Docker et exécutez le conteneur :
    ```sh
    docker build -t exaroton-reset .
    docker run --env-file .env exaroton-reset
    ```
   
### Option 2 : Exécution avec Docker Compose

> [!TIP]
> À mon avis, c'est la meilleure façon d'exécuter le conteneur en utilisant Docker Compose.

1. Créez un fichier `docker-compose.yml` dans le répertoire racine du projet avec le contenu suivant :

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


2. Exécutez la commande suivante pour démarrer le conteneur :
   Une autre façon d'exécuter le conteneur en utilisant Docker Compose est
   de passer le fichier `.env` dans la section `environment` du fichier `docker-compose.yml`.

    ```yaml
    version: '3.8'

    services:
      exaroton-reset:
        image: ghcr.io/sergisvk/exaroton-reset:latest
        env_file:
          - .env
        restart: unless-stopped
    ```

Cela démarrera le conteneur en utilisant la dernière image publiée dans le registre de conteneurs GitHub et les variables d'environnement définies dans le fichier `.env`.

## 🌱 Explication des Variables d'Environnement

- `TOKEN` : Il s'agit du jeton API Exaroton utilisé pour authentifier les requêtes à l'API Exaroton. Vous devez obtenir ce jeton depuis votre compte Exaroton.

- `TIMEZONE` : Le fuseau horaire dans lequel vous souhaitez planifier le démarrage du serveur. Il doit être au format [tz](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) reconnu (par exemple, `Europe/Paris`).

- `WEBHOOK_URL` : L'URL du webhook où les notifications seront envoyées. Cela peut être une URL de webhook Discord ou un autre service qui accepte les webhooks.

- `CRON_SCHEDULE_START` : Le programme cron pour démarrer le serveur. Dans ce cas, il est configuré pour démarrer le serveur tous les jours à 6h00 (`"0 6 * * *"`).

- `CRON_SCHEDULE_STOP` : Le programme cron pour arrêter le serveur. Dans ce cas, il est configuré pour arrêter le serveur tous les jours à 22h00 (`"0 22 * * *"`).

- `ID_SERVER` : L'ID de votre serveur Exaroton. Cet ID est unique pour chaque serveur et est utilisé pour identifier le serveur que vous souhaitez démarrer.

- `LANGUAGE` : La langue dans laquelle les notifications seront envoyées.
   Les langues disponibles sont `en-UK`, `es-ES`, `fr-FR`, `pt-PT`.

### Explication de la Fonctionnalité CRON

Le format cron est utilisé pour planifier des tâches à des intervalles spécifiques. La syntaxe d'une expression cron est la suivante :

```cmd
* * * * *
| | | | |
| | | | +---- Jour de la semaine (0 - 7) (Dimanche à Samedi, où 0 et 7 sont Dimanche)
| | | +------ Mois (1 - 12)
| | +-------- Jour du mois (1 - 31)
| +---------- Heure (0 - 23)
+------------ Minute (0 - 59)
```

Chaque champ peut contenir une ou plusieurs valeurs, séparées par des virgules. Les valeurs peuvent être des nombres spécifiques, des plages de nombres ou des caractères spéciaux tels que `*` (n'importe quelle valeur), `/` (incréments) et `-` (plages).

## 🤝 Contributions

Les contributions sont les bienvenues. Veuillez ouvrir un problème ou une demande de tirage pour discuter des modifications que vous souhaitez apporter.

[![Contributeurs sur GitHub](https://img.shields.io/github/contributors/sergisvk/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/pulls)
[![Issues sur GitHub](https://img.shields.io/github/issues/sergisvk/exaroton-reset)](https://github.com/SergiSvK/exaroton-reset/issues)

## 🪙 Donations

Ce projet est maintenu par SergiSvK. Si vous trouvez ce projet utile, envisagez de faire un don.

<div align="center">
  <table align="center">
    <tr>
      <td align="center">
        <a href="https://btcscan.org/address/3AWqbrfMp1Z36XPGNmuZQAmxWZmKDqKGjW" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg" alt="Logo BTC" width="50" height="50"/>
          <br/>
          <button>Donner BTC</button>
        </a>
      </td>
      <td align="center">
        <a href="https://etherscan.io/address/0x1D31ccEa10207FF603b0b837Ed8Fb47454aeeff6" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Ethereum-icon-purple.svg" alt="Logo ETH" width="50" height="50"/>
          <br/>
          <button>Donner ETH</button>
        </a>
      </td>
    </tr>
  </table>
</div>


## 📄 Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.
