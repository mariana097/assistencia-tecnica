from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import List, Optional

from .auth_router import verify_token

router = APIRouter(prefix="/ordens", tags=["Ordens"])

class OrdemCreate(BaseModel):
    cliente_id: int
    tecnico_id: Optional[int] = None
    aparelho_id: Optional[int] = None
    descricao_problema: str
    valor_total: float = 0.0
    status: Optional[str] = "ABERTA"

class OrdemUpdate(BaseModel):
    tecnico_id: Optional[int] = None
    aparelho_id: Optional[int] = None
    descricao_problema: Optional[str] = None
    valor_total: Optional[float] = None
    status: Optional[str] = None

class OrdemResponse(BaseModel):
    id: int
    cliente_id: int
    tecnico_id: Optional[int] = None
    aparelho_id: Optional[int] = None
    descricao_problema: str
    valor_total: float
    status: str
    data_abertura: datetime
    data_encerramento: Optional[datetime] = None

ordens_db = []
next_id = 1

@router.get("/", response_model=List[OrdemResponse])
def listar_ordens(_=Depends(verify_token)):
    """Listar todas as ordens de serviço"""
    return ordens_db

@router.post("/", response_model=OrdemResponse, status_code=status.HTTP_201_CREATED)
def criar_ordem(ordem: OrdemCreate, _=Depends(verify_token)):
    """Criar nova ordem de serviço"""
    global next_id
    agora = datetime.now(timezone.utc)
    nova_ordem = {
        "id": next_id,
        "cliente_id": ordem.cliente_id,
        "tecnico_id": ordem.tecnico_id,
        "aparelho_id": ordem.aparelho_id,
        "descricao_problema": ordem.descricao_problema,
        "valor_total": ordem.valor_total,
        "status": ordem.status or "ABERTA",
        "data_abertura": agora,
        "data_encerramento": None
    }
    ordens_db.append(nova_ordem)
    next_id += 1
    return nova_ordem

@router.get("/{ordem_id}", response_model=OrdemResponse)
def buscar_ordem(ordem_id: int, _=Depends(verify_token)):
    """Buscar ordem de serviço por ID"""
    for ordem in ordens_db:
        if ordem["id"] == ordem_id:
            return ordem
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ordem de serviço não encontrada")

@router.put("/{ordem_id}", response_model=OrdemResponse)
def atualizar_ordem(ordem_id: int, data: OrdemUpdate, _=Depends(verify_token)):
    """Atualizar ordem de serviço"""
    for i, ordem in enumerate(ordens_db):
        if ordem["id"] == ordem_id:
            atualizado = {**ordem}
            if data.tecnico_id is not None:
                atualizado["tecnico_id"] = data.tecnico_id
            if data.aparelho_id is not None:
                atualizado["aparelho_id"] = data.aparelho_id
            if data.descricao_problema is not None:
                atualizado["descricao_problema"] = data.descricao_problema
            if data.valor_total is not None:
                atualizado["valor_total"] = data.valor_total
            if data.status is not None:
                atualizado["status"] = data.status
            if data.status.upper() == "ENCERRADA" and atualizado["data_encerramento"] is None:
                atualizado["data_encerramento"] = datetime.now(timezone.utc)
            ordens_db[i] = atualizado
            return atualizado
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ordem de serviço não encontrada")

@router.patch("/{ordem_id}/encerrar", response_model=OrdemResponse)
def encerrar_ordem(ordem_id: int, _=Depends(verify_token)):
    """Encerrar ordem de serviço"""
    for i, ordem in enumerate(ordens_db):
        if ordem["id"] == ordem_id:
            if ordem["status"] != "ENCERRADA":
                ordens_db[i]["status"] = "ENCERRADA"
                ordens_db[i]["data_encerramento"] = datetime.now(timezone.utc)
            return ordens_db[i]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ordem de serviço não encontrada")

@router.delete("/{ordem_id}")
def cancelar_ordem(ordem_id: int, _=Depends(verify_token)):
    """Cancelar ordem de serviço"""
    for i, ordem in enumerate(ordens_db):
        if ordem["id"] == ordem_id:
            ordens_db[i]["status"] = "CANCELADA"
            return {"message": "Ordem de serviço cancelada com sucesso"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ordem de serviço não encontrada")
