from fastapi import FastAPI
import torch

app = FastAPI(title="Oncologie RAG Agent API")

@app.get("/")
def read_root():
    # On vérifie si votre moteur peut voir votre carte graphique (si présente) 
    # ou s'il tourne sur le processeur (CPU)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    return {
        "status": "online",
        "agent": "Oncologie-RAG",
        "engine": f"Running on {device}",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}