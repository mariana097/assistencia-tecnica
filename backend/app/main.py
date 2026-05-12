from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth_router, usuario_router, funcionario_router
from app.routers.api_router import api_router

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