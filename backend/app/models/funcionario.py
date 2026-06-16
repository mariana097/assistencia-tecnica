from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from datetime import datetime
from backend.app.database import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    cargo = Column(String(50), nullable=False)
    telefone = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    ativo = Column(Boolean, default=True)

    def __init__(
        self,
        id: int = None,
        nome: str = None,
        email: str = None,
        cargo: str = None,
        telefone: str = None,
        salario: float = 0.0,
        especialidade: str = None,
        nivel_experiencia: int = 1,
        comissao_percentual: float = 0.0,
        cpf: str = None,
        senha: str = None
    ):
        self.id = id
        self.nome = nome
        self.email = email
        self.cargo = cargo
        self.telefone = telefone
        self.salario = salario
        self.especialidade = especialidade
        self.nivel_experiencia = nivel_experiencia
        self.comissao_percentual = comissao_percentual
        self.cpf = cpf
        self.senha = senha
        self.created_at = datetime.now()
        self.ativo = True

        if self.nivel_experiencia < 1 or self.nivel_experiencia > 5:
            raise ValueError("Nível de experiência deve ser entre 1 e 5")
        if self.comissao_percentual < 0 or self.comissao_percentual > 30:
            raise ValueError("Comissão deve ser entre 0% e 30%")

    def calcular_comissao(self, valor_servico: float) -> float:
        return valor_servico * (self.comissao_percentual / 100)

    def iniciar_execucao_servico(self, servico_executado_id: int) -> dict:
        return {
            "servico_executado_id": servico_executado_id,
            "tecnico_id": self.id,
            "data_inicio": datetime.now(),
            "status": "EM_EXECUCAO"
        }

    def finalizar_execucao_servico(self, servico_executado_id: int, tempo_gasto: float) -> dict:
        return {
            "servico_executado_id": servico_executado_id,
            "tecnico_id": self.id,
            "data_fim": datetime.now(),
            "tempo_gasto": tempo_gasto,
            "status": "CONCLUIDO"
        }
