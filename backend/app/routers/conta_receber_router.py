from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from .auth_router import verify_token

router = APIRouter(prefix="/contas_receber", tags=["ContasReceber"])

class ContaReceberCreate(BaseModel):
    os_id: int
    cliente_id: int
    valor_original: float
    multa: float = 0.0
    juros: float = 0.0
    valor_total: float
    data_emissao: datetime
    data_vencimento: datetime

class ContaReceberResponse(ContaReceberCreate):
    id: int
    status_pagamento: str
    valor_pago: float = 0.0
    forma_pagamento: Optional[str] = None
    transacao_id: Optional[str] = None
    data_pagamento: Optional[datetime] = None

class PagamentoRequest(BaseModel):
    valor_pago: float
    forma_pagamento: str
    transacao_id: str

contas_receber_db = []
next_id = 1

@router.get("/", response_model=List[ContaReceberResponse])
def listar_contas_receber(_=Depends(verify_token)):
    """Listar todas as contas a receber"""
    return contas_receber_db

@router.post("/", response_model=ContaReceberResponse, status_code=status.HTTP_201_CREATED)
def criar_conta_receber(data: ContaReceberCreate, _=Depends(verify_token)):
    """Criar nova conta a receber"""
    global next_id
    conta = {
        "id": next_id,
        "os_id": data.os_id,
        "cliente_id": data.cliente_id,
        "valor_original": data.valor_original,
        "multa": data.multa,
        "juros": data.juros,
        "valor_total": data.valor_total,
        "valor_pago": 0.0,
        "data_emissao": data.data_emissao,
        "data_vencimento": data.data_vencimento,
        "data_pagamento": None,
        "status_pagamento": "PENDENTE",
        "forma_pagamento": None,
        "transacao_id": None,
        "os_id": data.os_id
    }
    contas_receber_db.append(conta)
    next_id += 1
    return conta

@router.get("/{conta_id}", response_model=ContaReceberResponse)
def buscar_conta_receber(conta_id: int, _=Depends(verify_token)):
    """Buscar conta a receber por ID"""
    for conta in contas_receber_db:
        if conta["id"] == conta_id:
            return conta
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta a receber não encontrada")

@router.post("/{conta_id}/pagar", response_model=ContaReceberResponse)
def pagar_conta_receber(conta_id: int, data: PagamentoRequest, _=Depends(verify_token)):
    """Registrar pagamento de conta a receber"""
    for conta in contas_receber_db:
        if conta["id"] == conta_id:
            conta["status_pagamento"] = "PAGO"
            conta["valor_pago"] = data.valor_pago
            conta["forma_pagamento"] = data.forma_pagamento
            conta["transacao_id"] = data.transacao_id
            conta["data_pagamento"] = datetime.now()
            return conta
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta a receber não encontrada")
