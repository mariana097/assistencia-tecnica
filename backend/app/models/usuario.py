from datetime import datetime
from typing import Optional

class Usuario:
    def __init__(
        self,
        id: Optional[int] = None,
        email: str = None,
        senha: str = None,
        nome: str = None,
        status: str = "ATIVO",
        created_at: datetime = None
    ):
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.status = status
        self.created_at = created_at or datetime.now()
    
    def autenticar(self, senha: str) -> bool:
        """Verifica se a senha está correta"""
        return self.senha == senha
    
    def alterar_senha(self, nova_senha: str) -> bool:
        """Altera a senha do usuário"""
        if len(nova_senha) < 6:
            raise ValueError("Senha deve ter no mínimo 6 caracteres")
        self.senha = nova_senha
        return True
    
    def desativar(self):
        """Desativa o usuário"""
        self.status = "INATIVO"
    
    def ativar(self):
        """Ativa o usuário"""
        self.status = "ATIVO"
    
    def to_dict(self):
        """Converte para dicionário"""
        return {
            "id": self.id,
            "email": self.email,
            "nome": self.nome,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    @staticmethod
    def criptografar_senha(senha: str) -> str:
        """Criptografa a senha (simplificado para testes)"""
        return senha  # Em produção, use bcrypt
