from backend.app.models.ordem_servico import OrdemServico
from backend.app.models.conta_receber import ContaReceber
from datetime import datetime, timedelta


class OrdemServicoService:

    @staticmethod
    def abrir_os(db, data):
        os = OrdemServico(
            descricao=data.descricao,
            cliente_id=data.cliente_id,
            aparelho_id=data.aparelho_id,
            status="ABERTA",
            data_abertura=datetime.now()
        )

        db.add(os)
        db.commit()
        db.refresh(os)
        return os

    @staticmethod
    def finalizar_os(db, os_id: int):
        os = db.query(OrdemServico).get(os_id)

        if not os:
            raise ValueError("OS não encontrada")

        if os.status == "FINALIZADA":
            raise ValueError("OS já finalizada")

        os.status = "FINALIZADA"
        os.data_fechamento = datetime.now()

        # 🔥 REGRA IMPORTANTE: gera conta automaticamente
        conta = ContaReceber(
            ordem_servico_id=os.id,
            valor_total=0,  # será calculado depois
            data_vencimento=datetime.now().date() + timedelta(days=30),
            status="PENDENTE"
        )

        db.add(conta)
        db.commit()

        return os