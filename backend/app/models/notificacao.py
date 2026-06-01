from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from backend.app.database import Base

class Notificacao(Base):
    __tablename__ = "notificacao"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=False)
    tipo = Column(String(20), default="INFO", nullable=False)
    titulo = Column(String(100), nullable=False)
    mensagem = Column(String(500), nullable=False)
    data_envio = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    data_leitura = Column(DateTime(timezone=True), nullable=True)
    status = Column(String(20), default="PENDENTE", nullable=False)
    link_referencia = Column(String(255), nullable=True)
