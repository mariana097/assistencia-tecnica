from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String, nullable=False)
    contato = Column(String(50), nullable=False)
    horario = Column(String(100), nullable=True)
    salario = Column(Float, nullable=True)
    cnpj = Column(String(14), nullable=True)
    ativo = Column(Boolean, default=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())

    usuario = relationship("Usuario", back_populates="funcionarios")

    def __repr__(self):
        return f"<Funcionario(id={self.id}, nome={self.nome})>"