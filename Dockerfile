# Utilisez l'image Python officielle en tant qu'image de base
FROM python:3.8-slim

# Créez un répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers Python nécessaires dans le conteneur
COPY endpoints.py main.py ./

# Installez les dépendances Python
RUN pip install requests

# Commande par défaut pour exécuter le script Python
CMD ["python", "main.py"]
