from pydantic import BaseModel
from typing import Optional


class OrdemServicoServicoBase(BaseModel):
    ordem_servico_id: int
    servico_id: int
    quantidade: int
    valor_aplicado: float


class OrdemServicoServicoCreate(OrdemServicoServicoBase):
    pass


class OrdemServicoServicoResponse(OrdemServicoServicoBase):
    id: int

    class Config:
        from_attributes = True