from fastapi import FastAPI
from pydantic import BaseModel
import torch

app = FastAPI(title="Projet HOPE - Serveur d'Inférence")

class MedicalQuery(BaseModel):
    text: str

@app.get("/")
def read_root():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return {
        "moteur": "Agent IA Hope",
        "statut": "Opérationnel",
        "device": device
    }

@app.post("/analyse")
async def analyse_cas(query: MedicalQuery):
    # Simulation d'analyse pour le moment
    # Ici viendra plus tard l'appel au modèle d'IA (LLM)
    return {
        "analyse": f"Réception du cas : {query.text[:50]}...",
        "moteur_utilise": "GTX 1650 (CUDA)" if torch.cuda.is_available() else "CPU",
        "note": "Système prêt pour l'ingestion de documents de recherche."
    }