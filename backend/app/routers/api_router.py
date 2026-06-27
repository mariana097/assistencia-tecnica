from fastapi import APIRouter, Depends
from backend.app.routers import auth_router, funcionario_router, cliente_router, ordem_servico_router
from backend.app.routers import servico_router, conta_receber_router, auditoria_router

api_router = APIRouter(prefix="/api")

# Incluir todos os routers com prefixo /api
api_router.include_router(auth_router)
api_router.include_router(funcionario_router)
api_router.include_router(cliente_router)
api_router.include_router(ordem_servico_router)
api_router.include_router(servico_router)
api_router.include_router(conta_receber_router)
api_router.include_router(pagamento_router)
api_router.include_router(auditoria_router)
