from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional

class FuncionarioBase(BaseModel):
    nome: str
    email: EmailStr
    cargo: str
    telefone: str

class FuncionarioCreate(FuncionarioBase):
    senha: str

class FuncionarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    cargo: Optional[str] = None
    telefone: Optional[str] = None

class FuncionarioResponse(FuncionarioBase):
    id: int
    ativo: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
