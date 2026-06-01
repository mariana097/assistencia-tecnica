from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from backend.app.database import Base

class OrdemServico(Base):
    __tablename__ = "ordem_servico"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, nullable=False)
    tecnico_id = Column(Integer, nullable=True)
    aparelho_id = Column(Integer, nullable=True)
    descricao_problema = Column(String(255), nullable=False)
    valor_total = Column(Float, default=0.0, nullable=False)
    status = Column(String(20), default="ABERTA", nullable=False)
    data_abertura = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    data_encerramento = Column(DateTime(timezone=True), nullable=True)
