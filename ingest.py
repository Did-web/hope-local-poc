import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

# 1. Configuration automatique des chemins (s'adapte à l'endroit ou se trouve le script)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(BASE_DIR, "vectorstore_db")

print(f"✅ Dossier de travail détecté : {BASE_DIR}")


def create_vector_db():
    # On vérifie si le dossier data existe
    if not os.path.exists(DATA_PATH):
        print(f"Erreur : Le dossier {DATA_PATH} est introuvable.")
        return

    # 2. Chargement des PDF
    documents = []
    # On liste les fichiers pour déboguer
    fichiers = os.listdir(DATA_PATH)
    print(f"📂 Contenu du dossier data : {fichiers}") # Pour vérifier ce que Python voit

    for file in fichiers:
        # On accepte .pdf et .PDF
        if file.lower().endswith(".pdf"):
            print(f"📄 Lecture de : {file}")
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    # 3. Découpage du texte (Chunking)
    # On découpe par blocs de 2000 (1000 corrigé pour soulager GTX1650) caractères avec un chevauchement pour garder le contexte
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    print(f"✅ {len(chunks)} fragments de texte créés.")

    # 4. Création des Embeddings (Le cerveau numérique)
    # On utilise nomic-embed-text car ça ne passe pas avec OllamaEmbeddings(model="llama3.2")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")          
  

    ## 5. Stockage progressif dans ChromaDB
    print("🧠 Initialisation de la base de données...")
    vector_db = Chroma(
        embedding_function=embeddings,
        persist_directory=DB_PATH
    )

    # On ajoute les documents par petits lots (batches) de 20
    batch_size = 20
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        try:
            vector_db.add_documents(batch)
            print(f"✅ Progression : {i + len(batch)} / {len(chunks)} fragments indexés...")
        except Exception as e:
            print(f"⚠️ Petit souci au fragment {i}, on continue... Erreur : {e}")

    print(f"🚀 Terminé ! Base de connaissances sauvegardée dans : {DB_PATH}")

if __name__ == "__main__":
    create_vector_db()

