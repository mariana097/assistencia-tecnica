from sqlalchemy import Column, Integer, String, Float, DateTime
from backend.app.database import Base

class ContaReceber(Base):
    __tablename__ = "conta_receber"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, nullable=False)
    valor_original = Column(Float, default=0.0, nullable=False)
    multa = Column(Float, default=0.0, nullable=False)
    juros = Column(Float, default=0.0, nullable=False)
    valor_total = Column(Float, default=0.0, nullable=False)
    valor_pago = Column(Float, default=0.0, nullable=False)
    data_emissao = Column(DateTime(timezone=True), nullable=False)
    data_vencimento = Column(DateTime(timezone=True), nullable=False)
    data_pagamento = Column(DateTime(timezone=True), nullable=True)
    status_pagamento = Column(String(20), default="PENDENTE", nullable=False)
    forma_pagamento = Column(String(50), nullable=True)
    transacao_id = Column(String(100), nullable=True)
    qr_code_pix = Column(String(255), nullable=True)
    boleto_codigo = Column(String(255), nullable=True)
    os_id = Column(Integer, nullable=False)
