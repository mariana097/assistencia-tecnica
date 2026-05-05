from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Date
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(Text, nullable=False)
    contato = Column(String(50), nullable=False)
    tipo = Column(String(2), nullable=False)  # PF ou PJ
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())

    # Relacionamento com usuário
    usuario = relationship("Usuario", back_populates="clientes")

    # Dados específicos para PF
    cpf = Column(String(11), unique=True, nullable=True)
    data_nascimento = Column(Date, nullable=True)

    # Dados específicos para PJ (futuro)
    # cnpj = Column(String(14), unique=True, nullable=True)
    # razao_social = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Cliente(id={self.id}, nome={self.nome}, tipo={self.tipo})>"