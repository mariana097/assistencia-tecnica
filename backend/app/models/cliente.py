from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    telefone = Column(String(20), nullable=False)
    endereco = Column(String(200))
    data_cadastro = Column(DateTime(timezone=True), server_default=func.now())
    ativo = Column(Boolean, default=True)
