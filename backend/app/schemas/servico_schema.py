from pydantic import BaseModel
from typing import Optional


class ServicoBase(BaseModel):
    nome: str
    descricao: str
    valor_padrao: float
    ativo: bool = True


class ServicoCreate(ServicoBase):
    pass


class ServicoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    valor_padrao: Optional[float] = None
    ativo: Optional[bool] = None


class ServicoResponse(ServicoBase):
    id: int

    class Config:
        from_attributes = True