from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.app.database import Base

class ServicoExecutado(Base):
    __tablename__ = "servico_executado"

    id = Column(Integer, primary_key=True, index=True)
    garantia_dias = Column(Integer, default=0, nullable=False)
    valor_cobrado = Column(Float, default=0.0, nullable=False)
    observacoes = Column(String(255), nullable=True)
    os_id = Column(Integer, nullable=False)
    servico_id = Column(Integer, nullable=False)
    tecnico_id = Column(Integer, nullable=False)
    data_inicio = Column(DateTime(timezone=True), nullable=True)
    minutos_pausa = Column(Integer, default=0, nullable=False)
    data_fim = Column(DateTime(timezone=True), nullable=True)
    tempo_gasto = Column(Float, default=0.0, nullable=False)
    data_fim_garantia = Column(DateTime(timezone=True), nullable=True)
    status_execucao = Column(String(50), default="PENDENTE", nullable=False)
    comissao_calculada = Column(Float, default=0.0, nullable=False)
