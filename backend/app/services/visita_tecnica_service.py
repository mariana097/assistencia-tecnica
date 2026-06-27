from backend.app.models.visita_tecnica import VisitaTecnica
from datetime import datetime


class VisitaTecnicaService:

    @staticmethod
    def agendar(db, data):
        visita = VisitaTecnica(
            ordem_servico_id=data.ordem_servico_id,
            funcionario_id=data.funcionario_id,
            data_agendamento=data.data_agendamento,
            status="AGENDADA"
        )

        db.add(visita)
        db.commit()
        db.refresh(visita)
        return visita

    @staticmethod
    def registrar_execucao(db, visita_id: int, resultado: str):
        visita = db.query(VisitaTecnica).get(visita_id)

        visita.data_realizacao = datetime.now()
        visita.resultado = resultado
        visita.status = "CONCLUIDA"

        db.commit()
        return visita