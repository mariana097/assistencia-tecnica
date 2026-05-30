from fastapi import APIRouter, Depends
from app.routers import auth_router, usuario_router, funcionario_router, cliente_router, os_router

api_router = APIRouter(prefix="/api")

# Incluir todos os routers com prefixo /api
api_router.include_router(auth_router)
api_router.include_router(usuario_router)
api_router.include_router(funcionario_router)
api_router.include_router(cliente_router)
api_router.include_router(os_router)
