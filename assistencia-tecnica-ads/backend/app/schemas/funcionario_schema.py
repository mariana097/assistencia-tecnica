from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class FuncionarioCreate(BaseModel):
    nome: str
    endereco: str
    contato: str
    horario: Optional[str] = None
    salario: Optional[float] = None
    cnpj: Optional[str] = None
    ativo: Optional[bool] = True
    usuario_id: int

class FuncionarioUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    contato: Optional[str] = None
    horario: Optional[str] = None
    salario: Optional[float] = None
    cnpj: Optional[str] = None
    ativo: Optional[bool] = None

class FuncionarioResponse(BaseModel):
    id: int
    nome: str
    endereco: str
    contato: str
    horario: Optional[str]
    salario: Optional[float]
    cnpj: Optional[str]
    ativo: bool
    usuario_id: int
    criado_em: Optional[datetime]
    atualizado_em: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
from_attributes = True