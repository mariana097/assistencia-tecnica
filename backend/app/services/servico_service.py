from backend.app.models.servico import Servico


class ServicoService:

    @staticmethod
    def criar(db, data):
        servico = Servico(**data.dict())
        db.add(servico)
        db.commit()
        db.refresh(servico)
        return servico

    @staticmethod
    def listar(db):
        return db.query(Servico).all()

    @staticmethod
    def desativar(db, id: int):
        servico = db.query(Servico).get(id)

        if not servico:
            raise ValueError("Serviço não encontrado")

        servico.ativo = False
        db.commit()
        return servico