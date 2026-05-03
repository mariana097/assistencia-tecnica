from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional
from .usuario_schema import UsuarioResponse

# Schema para dados de pessoa física
class PessoaFisicaBase(BaseModel):
    cpf: str
    data_nascimento: date

# Schema para criação de cliente
class ClienteCreate(BaseModel):
    nome: str
    endereco: str
    contato: str
    tipo: str  # "PF" ou "PJ"
    usuario_id: int
    pf_data: Optional[PessoaFisicaBase] = None  # Dados específicos para PF

# Schema para atualização de cliente
class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    endereco: Optional[str] = None
    contato: Optional[str] = None
    tipo: Optional[str] = None
    pf_data: Optional[PessoaFisicaBase] = None

# Schema para resposta de cliente
class ClienteResponse(BaseModel):
    id: int
    nome: str
    endereco: str
    contato: str
    tipo: str
    usuario_id: int
    criado_em: Optional[datetime]
    atualizado_em: Optional[datetime]
    cpf: Optional[str]
    data_nascimento: Optional[date]
    usuario: Optional[UsuarioResponse] = None

    class Config:
        from_attributes = True