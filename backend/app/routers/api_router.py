from fastapi import APIRouter, Depends
from backend.app.routers import auth_router, usuario_router, funcionario_router, cliente_router, os_router
from backend.app.routers import equipamento_usado_router, conta_receber_router, notificacao_router

api_router = APIRouter(prefix="/api")

# Incluir todos os routers com prefixo /api
api_router.include_router(auth_router)
api_router.include_router(usuario_router)
api_router.include_router(funcionario_router)
api_router.include_router(cliente_router)
api_router.include_router(os_router)
api_router.include_router(equipamento_usado_router)
api_router.include_router(conta_receber_router)
api_router.include_router(notificacao_router)
