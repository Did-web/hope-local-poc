FROM python:3.10-slim

# Dépendances système pour Selenium (le futur bras armé de votre agent)
RUN apt-get update && apt-get install -y \
    wget gnupg unzip chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Mise à jour et installation des outils nécessaires (Dont curl et Ajout de zstd)
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    unzip \
    zstd \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# On installe votre "cerveau" (le fichier txt que vous venez de faire)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On prépare l'arrivée du code
COPY ./src /app/src

EXPOSE 8080
RUN curl -fsSL https://ollama.com/install.sh | sh
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]