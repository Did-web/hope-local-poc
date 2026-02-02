import sys
import os

# On force le chemin vers ton venv
sys.path.append(os.path.join(os.getcwd(), "venv/lib/python3.12/site-packages"))

from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

print("✅ Moteur de base chargé")

# Connexion à ta DB de 1916 fragments
DB_PATH = os.path.join(os.getcwd(), "vectorstore_db")
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector_db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
retriever = vector_db.as_retriever()

llm = OllamaLLM(model="llama3.2")

# Le Prompt de Hope
template = """Tu es Hope. Réponds à la question en utilisant ce contexte :
{context}

Question : {question}"""
prompt = ChatPromptTemplate.from_template(template)

# Construction de la chaîne SANS utiliser 'langchain.chains'
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("🚀 Hope est prête. Interrogation...")
try:
    response = rag_chain.invoke("How does the homeostatic disruption affect the pituitary gland according to the documents?")
    print(f"\n🤖 Hope : {response}")
except Exception as e:
    print(f"❌ Erreur lors de l'appel : {e}")