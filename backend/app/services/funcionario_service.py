from backend.app.models.funcionario import Funcionario
from backend.app.core.database import SessionLocal
from datetime import datetime
import hashlib


class FuncionarioService:

    @staticmethod
    def criar_funcionario(data, db):
        # valida email duplicado
        existente = db.query(Funcionario).filter(Funcionario.email == data.email).first()
        if existente:
            raise ValueError("Email já cadastrado")

        funcionario = Funcionario(
            nome=data.nome,
            email=data.email,
            senha=FuncionarioService._hash_senha(data.senha),
            perfil=data.perfil,
            telefone=data.telefone,
            ativo=True
        )

        db.add(funcionario)
        db.commit()
        db.refresh(funcionario)

        return funcionario

    @staticmethod
    def listar_funcionarios(db):
        return db.query(Funcionario).all()

    @staticmethod
    def buscar_por_id(db, id: int):
        return db.query(Funcionario).filter(Funcionario.id == id).first()

    @staticmethod
    def desativar_funcionario(db, id: int):
        funcionario = FuncionarioService.buscar_por_id(db, id)

        if not funcionario:
            raise ValueError("Funcionário não encontrado")

        funcionario.ativo = False
        db.commit()

        return funcionario

    @staticmethod
    def _hash_senha(senha: str):
        return hashlib.sha256(senha.encode()).hexdigest()
    