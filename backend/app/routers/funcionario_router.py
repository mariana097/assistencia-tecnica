from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.schemas.funcionario_schema import FuncionarioCreate, FuncionarioUpdate
from backend.app.services.funcionario_service import FuncionarioService
from backend.app.database.deps import get_db

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])

@router.post("/")
def create(data: FuncionarioCreate, db: Session = Depends(get_db)):
    return FuncionarioService.create(db, data)

@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return FuncionarioService.list_all(db)

@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    return FuncionarioService.get_by_id(db, id)

@router.put("/{id}")
def update(id: int, data: FuncionarioUpdate, db: Session = Depends(get_db)):
    return FuncionarioService.update(db, id, data)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return FuncionarioService.delete(db, id)