from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List, Optional

from .auth_router import verify_token

router = APIRouter(prefix="/equipamentos_usado", tags=["EquipamentosUsados"])

class EquipamentoUsadoCreate(BaseModel):
    servico_executado_id: int
    equipamento_id: int
    quantidade: int = 1
    horas_utilizadas: float = 0.0
    observacoes: Optional[str] = None

class EquipamentoUsadoResponse(EquipamentoUsadoCreate):
    id: int

# Dados em memória
equipamentos_usado_db = []
next_id = 1

@router.get("/", response_model=List[EquipamentoUsadoResponse])
def listar_equipamentos_usados(_=Depends(verify_token)):
    """Listar todos os equipamentos utilizados em serviços"""
    return equipamentos_usado_db

@router.post("/", response_model=EquipamentoUsadoResponse, status_code=status.HTTP_201_CREATED)
def criar_equipamento_usado(data: EquipamentoUsadoCreate, _=Depends(verify_token)):
    """Registrar equipamento utilizado em um serviço executado"""
    global next_id
    equipamento_usado = {
        "id": next_id,
        "servico_executado_id": data.servico_executado_id,
        "equipamento_id": data.equipamento_id,
        "quantidade": data.quantidade,
        "horas_utilizadas": data.horas_utilizadas,
        "observacoes": data.observacoes
    }
    equipamentos_usado_db.append(equipamento_usado)
    next_id += 1
    return equipamento_usado

@router.get("/{equipamento_usado_id}", response_model=EquipamentoUsadoResponse)
def buscar_equipamento_usado(equipamento_usado_id: int, _=Depends(verify_token)):
    """Buscar equipamento usado por ID"""
    for equipamento in equipamentos_usado_db:
        if equipamento["id"] == equipamento_usado_id:
            return equipamento
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipamento usado não encontrado")

@router.delete("/{equipamento_usado_id}")
def remover_equipamento_usado(equipamento_usado_id: int, _=Depends(verify_token)):
    """Remover equipamento utilizado de um serviço"""
    for i, equipamento in enumerate(equipamentos_usado_db):
        if equipamento["id"] == equipamento_usado_id:
            del equipamentos_usado_db[i]
            return {"message": "Equipamento usado removido com sucesso"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipamento usado não encontrado")
