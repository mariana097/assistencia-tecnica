from backend.app.models.cliente import Cliente


class ClienteService:

    @staticmethod
    def criar_cliente(db, data):
        cliente = Cliente(**data.dict())
        db.add(cliente)
        db.commit()
        db.refresh(cliente)
        return cliente

    @staticmethod
    def listar(db):
        return db.query(Cliente).all()

    @staticmethod
    def desativar(db, id: int):
        cliente = db.query(Cliente).get(id)

        if not cliente:
            raise ValueError("Cliente não encontrado")

        cliente.ativo = False
        db.commit()
        return cliente