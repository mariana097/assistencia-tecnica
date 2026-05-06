from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional

# Schema para criação de usuário
class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str

# Schema para login
class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str

# Schema para resposta (não retorna a senha)
class UsuarioResponse(BaseModel):
    id: int
    email: EmailStr
    criado_em: Optional[datetime]
    atualizado_em: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
from_attributes = True

# Schema para token JWT
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
