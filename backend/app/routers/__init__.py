from .auth_router import router as auth_router
from .usuario_router import router as usuario_router
from .funcionario_router import router as funcionario_router
from .cliente_router import router as cliente_router
from .os_router import router as os_router

__all__ = ["auth_router", "usuario_router", "funcionario_router", "cliente_router", "os_router"]
