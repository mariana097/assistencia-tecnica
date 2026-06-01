from sqlalchemy import Column, Integer, String, Float
from backend.app.database import Base

class EquipamentoUsado(Base):
    __tablename__ = "equipamento_usado"

    id = Column(Integer, primary_key=True, index=True)
    horas_utilizadas = Column(Float, default=0.0, nullable=False)
    observacoes = Column(String(255), nullable=True)
    quantidade = Column(Integer, default=1, nullable=False)
    servico_executado_id = Column(Integer, nullable=False)
    equipamento_id = Column(Integer, nullable=False)
