from typing import Optional
from datetime import datetime
from .funcionario import Funcionario

class Tecnico(Funcionario):
    def __init__(
        self,
        id: Optional[int] = None,
        email: str = None,
        senha: str = None,
        nome: str = None,
        cpf: str = None,
        telefone: str = None,
        cargo: str = "TECNICO",
        salario: float = 0,
        especialidade: str = None,
        nivel_experiencia: int = 1,
        comissao_percentual: float = 0
    ):
        # Chama __init__ da classe pai corretamente
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cargo = cargo
        self.salario = salario
        self.especialidade = especialidade
        self.nivel_experiencia = nivel_experiencia
        self.comissao_percentual = comissao_percentual
        
        # Validações
        if nivel_experiencia < 1 or nivel_experiencia > 5:
            raise ValueError("Nível de experiência deve ser entre 1 e 5")
        if comissao_percentual < 0 or comissao_percentual > 30:
            raise ValueError("Comissão deve ser entre 0% e 30%")
    
    def calcular_comissao(self, valor_servico: float) -> float:
        """Calcula comissão baseada no valor do serviço"""
        return valor_servico * (self.comissao_percentual / 100)
    
    def iniciar_execucao_servico(self, servico_executado_id: int) -> dict:
        """Inicia a execução de um serviço"""
        return {
            "servico_executado_id": servico_executado_id,
            "tecnico_id": self.id,
            "data_inicio": datetime.now(),
            "status": "EM_EXECUCAO"
        }
    
    def finalizar_execucao_servico(self, servico_executado_id: int, tempo_gasto: float) -> dict:
        """Finaliza a execução de um serviço"""
        return {
            "servico_executado_id": servico_executado_id,
            "tecnico_id": self.id,
            "data_fim": datetime.now(),
            "tempo_gasto": tempo_gasto,
            "status": "CONCLUIDO"
        }
