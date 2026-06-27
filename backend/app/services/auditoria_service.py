from backend.app.models.auditoria_log import AuditoriaLog
from datetime import datetime


class AuditoriaService:

    @staticmethod
    def registrar(db, funcionario_id: int, acao: str, entidade: str):
        log = AuditoriaLog(
            funcionario_id=funcionario_id,
            acao=acao,
            entidade=entidade,
            data_hora=datetime.now()
        )

        db.add(log)
        db.commit()
        return log

    @staticmethod
    def listar(db):
        return db.query(AuditoriaLog).all()