from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# Importar routers
from app.routers import (
    auth_router,
    cliente_router,
    funcionario_router,
    usuario_router,
    relatorio_router
)

app = FastAPI(
    title="API Assistência Técnica",
    description="Sistema completo para gestão de assistência técnica",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas principais
@app.get("/")
async def root():
    return {
        "message": "Sistema de Gestão de Assistência Técnica",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "auth": "/auth",
            "clientes": "/clientes",
            "funcionarios": "/funcionarios",
            "usuarios": "/usuarios",
            "relatorios": "/relatorios",
            "dashboard": "/relatorios/dashboard/resumo"
        }
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

# Incluir routers
app.include_router(auth_router.router)
app.include_router(cliente_router.router)
app.include_router(funcionario_router.router)
app.include_router(usuario_router.router)
app.include_router(relatorio_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
