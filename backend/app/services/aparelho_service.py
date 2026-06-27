from backend.app.models.aparelho import Aparelho


class AparelhoService:

    @staticmethod
    def criar(db, data):
        aparelho = Aparelho(**data.dict())
        db.add(aparelho)
        db.commit()
        db.refresh(aparelho)
        return aparelho

    @staticmethod
    def listar_por_cliente(db, cliente_id: int):
        return db.query(Aparelho).filter(Aparelho.cliente_id == cliente_id).all()