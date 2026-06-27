from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VisitaTecnicaBase(BaseModel):
    ordem_servico_id: int
    funcionario_id: Optional[int] = None
    data_agendamento: datetime
    resultado: Optional[str] = None
    status: str = "AGENDADA"


class VisitaTecnicaCreate(VisitaTecnicaBase):
    pass


class VisitaTecnicaUpdate(BaseModel):
    data_agendamento: Optional[datetime] = None
    data_realizacao: Optional[datetime] = None
    resultado: Optional[str] = None
    status: Optional[str] = None


class VisitaTecnicaResponse(VisitaTecnicaBase):
    id: int
    data_realizacao: Optional[datetime]

    class Config:
        from_attributes = True