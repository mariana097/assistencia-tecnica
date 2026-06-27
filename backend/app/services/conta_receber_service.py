from backend.app.models.conta_receber import ContaReceber
from datetime import datetime


class ContaReceberService:

    @staticmethod
    def pagar_conta(db, conta_id: int):
        conta = db.query(ContaReceber).get(conta_id)

        if not conta:
            raise ValueError("Conta não encontrada")

        if conta.status == "PAGO":
            raise ValueError("Conta já paga")

        conta.status = "PAGO"
        conta.data_pagamento = datetime.now()

        db.commit()
        return conta