from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.database import Base, engine
import backend.app.models.cliente  # noqa: F401
import backend.app.models.funcionario  # noqa: F401
import backend.app.models.ordem_servico  # noqa: F401
import backend.app.models.servico_executado  # noqa: F401
import backend.app.models.equipamento_usado  # noqa: F401
import backend.app.models.conta_receber  # noqa: F401
import backend.app.models.notificacao  # noqa: F401

from backend.app.routers import auth_router, usuario_router, funcionario_router
from backend.app.routers import relatorio_router
from backend.app.routers.api_router import api_router

app = FastAPI(
    title="Sistema de Gestão de Assistência Técnica",
    description="API para gestão de assistência técnica",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# =========================
# ROUTERS
# =========================
app.include_router(auth_router)
app.include_router(usuario_router)
app.include_router(funcionario_router)
app.include_router(api_router)
app.include_router(relatorio_router)

# Ensure database tables exist before serving requests
Base.metadata.create_all(bind=engine)

# =========================
# ENDPOINTS
# =========================
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