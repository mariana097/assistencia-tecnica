from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Funcionario, Usuario
from ..schemas import FuncionarioCreate, FuncionarioResponse, FuncionarioUpdate
from ..routers.auth_router import oauth2_scheme
from ..utils import decodificar_token

router = APIRouter()

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decodificar_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")
    return payload.get("sub")

# 🔹 CREATE (salvar)
@router.post("/", response_model=FuncionarioResponse)
def criar(data: FuncionarioCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    novo = Funcionario(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# 🔹 LISTAR TODOS
@router.get("/", response_model=List[FuncionarioResponse])
def listar(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Funcionario).join(Usuario).filter(Usuario.email == user).all()

# 🔹 CONSULTAR (por id)
@router.get("/{id}", response_model=FuncionarioResponse)
def consultar(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    funcionario = db.query(Funcionario).join(Usuario).filter(
        Funcionario.id == id,
        Usuario.email == user
    ).first()

    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    return funcionario

# 🔹 UPDATE (salvar com id)
@router.put("/{id}", response_model=FuncionarioResponse)
def atualizar(id: int, data: FuncionarioUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    funcionario = db.query(Funcionario).join(Usuario).filter(
        Funcionario.id == id,
        Usuario.email == user
    ).first()

    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    update_data = data.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(funcionario, field, value)

    db.commit()
    db.refresh(funcionario)
    return funcionario

# 🔹 DELETE (excluir)
@router.delete("/{id}")
def excluir(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    funcionario = db.query(Funcionario).join(Usuario).filter(
        Funcionario.id == id,
        Usuario.email == user
    ).first()

    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    db.delete(funcionario)
    db.commit()

    return {"message": "Funcionário excluído com sucesso"}