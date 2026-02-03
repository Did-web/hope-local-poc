#!/bin/bash
docker rm -f hope-live
sudo systemctl stop ollama

docker run -d \
  --name hope-live \
  --gpus all \
  -p 8000:8000 -p 11434:11434 \
  -e OLLAMA_NUM_PARALLEL=1 \
  -v $(pwd):/app \
  hope-backup-stable \
  sh -c "ollama serve & sleep 15 && ollama pull nomic-embed-text && uvicorn src.main:app --host 0.0.0.0 --port 8000"

echo "Optimisation VRAM pour GTX 1650 en cours... (60 secondes)"
sleep 60