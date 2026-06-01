from .auth_router import router as auth_router
from .usuario_router import router as usuario_router
from .funcionario_router import router as funcionario_router
from .cliente_router import router as cliente_router
from .ordem_servico_router import router as os_router
from .equipamento_usado_router import router as equipamento_usado_router
from .conta_receber_router import router as conta_receber_router
from .notificacao_router import router as notificacao_router
from .relatorio_router import router as relatorio_router

__all__ = [
    "auth_router",
    "usuario_router",
    "funcionario_router",
    "cliente_router",
    "ordem_servico_router",
    "equipamento_usado_router",
    "conta_receber_router",
    "notificacao_router",
    "relatorio_router"
]
