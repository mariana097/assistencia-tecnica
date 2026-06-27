from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AuditoriaLogBase(BaseModel):
    funcionario_id: Optional[int]
    acao: str
    entidade: str


class AuditoriaLogCreate(AuditoriaLogBase):
    pass


class AuditoriaLogResponse(AuditoriaLogBase):
    id: int
    data_hora: datetime

    class Config:
        from_attributes = True