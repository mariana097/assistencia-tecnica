from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# =========================
# LOGIN
# =========================
class LoginSchema(BaseModel):
    email: EmailStr = Field(..., example="henrique@email.com")
    senha: str = Field(..., min_length=6, example="123456")


# =========================
# RESPOSTA DO TOKEN
# =========================
class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"


# =========================
# DADOS DO USUÁRIO LOGADO
# =========================
class UsuarioLogadoSchema(BaseModel):
    id: int
    nome: str
    email: EmailStr
    perfil: str


# =========================
# REGISTRO (caso use cadastro de funcionário)
# =========================
class RegisterSchema(BaseModel):
    nome: str = Field(..., min_length=3)
    email: EmailStr
    senha: str = Field(..., min_length=6)
    perfil: Optional[str] = "tecnico"