#!/bin/bash
# Matar processos antigos na porta 8000
echo "Parando servidores antigos..."
fuser -k 8000/tcp 2>/dev/null

# Aguardar 2 segundos
sleep 2

# Iniciar servidor
echo "Iniciando servidor na porta 8000..."
cd /workspaces/assistencia-tecnica-adm/assistencia-tecnica-ads/backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

echo "Servidor rodando em: http://localhost:8000"
