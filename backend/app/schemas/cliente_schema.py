from pydantic import BaseModel
from typing import Optional


class ClienteBase(BaseModel):
    nome: str
    documento: str  # CPF/CNPJ
    endereco: str
    contato: str
    ativo: bool = True


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    documento: Optional[str] = None
    endereco: Optional[str] = None
    contato: Optional[str] = None
    ativo: Optional[bool] = None


class ClienteResponse(ClienteBase):
    id: int

    class Config:
        from_attributes = True