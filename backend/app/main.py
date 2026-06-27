from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

# Importa os models para registrar as tabelas
from app.models import (
    funcionario,
    cliente,
    servico,
    equipamento,
    aparelho,
    ordem_servico,
    ordem_servico_servico,
    visita_tecnica,
    conta_receber,
    auditoria_log,
)

from backend.app.routers import (
    auth_router,
    funcionario_router,
    cliente_router,
    ordem_servico_router,
    servico_router,
    pagamento_router,
    auditoria_router
)

app = FastAPI(title="Sistema Assistência Técnica")

app.include_router(auth_router.router)
app.include_router(funcionario_router.router)
app.include_router(cliente_router.router)
app.include_router(ordem_servico_router.router)
app.include_router(servico_router.router)
app.include_router(pagamento_router.router)
app.include_router(auditoria_router.router)

app = FastAPI(
    title="Sistema de Gestão de Assistência Técnica",
    description="API para gestão de assistência técnica",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Bem-vindo ao Sistema de Gestão de Assistência Técnica"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "API está funcionando!"
    }