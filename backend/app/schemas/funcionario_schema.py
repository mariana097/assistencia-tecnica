from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class FuncionarioBase(BaseModel):
    nome: str
    email: EmailStr
    cargo: str
    telefone: str
    ativo: bool = True


class FuncionarioCreate(FuncionarioBase):
    senha: str


class FuncionarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    cargo: Optional[str] = None
    telefone: Optional[str] = None
    ativo: Optional[bool] = None


class FuncionarioResponse(FuncionarioBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
