from backend.app.models.equipamento import Equipamento


class EquipamentoService:

    @staticmethod
    def criar(db, data):
        eq = Equipamento(**data.dict())
        db.add(eq)
        db.commit()
        db.refresh(eq)
        return eq

    @staticmethod
    def desativar(db, id: int):
        eq = db.query(Equipamento).get(id)

        if not eq:
            raise ValueError("Equipamento não encontrado")

        eq.ativo = False
        db.commit()
        return eq