# KaraManager

KaraManager est une application web Flask pour gérer les clients, les salles et les commandes d'un karaoké.

## Prérequis

- Python 3.x
- pip

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votre-utilisateur/KaraManager.git
    cd KaraManager
    ```

2. Créez et activez un environnement virtuel :
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # Sur Windows, utilisez `.venv\Scripts\activate`
    ```

3. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

1. Lancez le serveur de développement :
    ```sh
    ./devserver.sh
    ```

2. Ouvrez votre navigateur et accédez à `http://localhost:5000`.

## Structure du projet

- `main.py` : Point d'entrée de l'application Flask.
- `database_manager.py` : Gestionnaire de base de données SQLite.
- `templates/` : Dossiers contenant les templates HTML.
- `static/` : Dossiers contenant les fichiers CSS et les images.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.