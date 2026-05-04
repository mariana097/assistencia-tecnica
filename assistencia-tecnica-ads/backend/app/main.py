# Ponto de entrada da aplicação
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import config
from .database import engine, Base
from .routers import auth_router, cliente_router

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criar instância do FastAPI
app = FastAPI(
    title=config.APP_NAME,
    description="API para gerenciar clientes, ordens de serviço e visitas técnicas",
    version=config.APP_VERSION,
    debug=config.DEBUG
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir roteadores
app.include_router(auth_router.router, prefix="/api/auth", tags=["Autenticação"])
app.include_router(cliente_router.router, prefix="/api/clientes", tags=["Clientes"])

# Rota raiz
@app.get("/")
def root():
    return {
        "message": f"Bem-vindo ao {config.APP_NAME}",
        "status": "online",
        "version": config.APP_VERSION
    }

# Rota de saúde
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Rota de informações
@app.get("/api/info")
def get_info():
    return {
        "nome": config.APP_NAME,
        "versao": config.APP_VERSION,
        "endpoints_planejados": [
            "/api/auth/login",
            "/api/auth/register",
            "/api/auth/me",
            "/api/clientes",
            "/api/funcionarios",
            "/api/os",
            "/api/equipamentos",
            "/api/visitas",
            "/api/contas"
        ]
    }
