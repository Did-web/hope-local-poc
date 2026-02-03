# Hope - Agent IA Oncologie (RAG)

Ce projet contient l'infrastructure Docker pour l'agent IA **Hope**, spécialisé en cancérologie, tournant sur **Atlas2** avec support GPU.

## 🔬 Capacité RAG & Intelligence Multilingue
Le système démontre une robustesse particulière dans la gestion des flux "Cross-Language" :
* **Base de connaissance** : Indexation de la thèse de B. Spada (2025) découpée en **277 fragments sémantiques**.
* **Performance Multilingue** : Hope est capable d'analyser une source technique en **anglais**, de traiter une requête utilisateur en **anglais**, et de générer une réponse médicale structurée en **italien**.
* **Précision** : Cette architecture garantit que l'agent capture les concepts (ex: l'oncologie comparée et l'évolution) au-delà des barrières linguistiques.

## 🛠 Pré-requis
- Système : Linux (Ubuntu/Debian conseillé)
- Matériel : GPU NVIDIA (testé sur GTX 1650 4Go)
- Logiciels : Docker + NVIDIA Container Toolkit

## 🚀 Installation & Déploiement

### 1. Récupérer le projet
```bash
git clone https://github.com/Did-web/oncologie-rag-agent.git
cd oncologie-rag-agent