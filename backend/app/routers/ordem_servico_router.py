from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.schemas.ordem_servico_schema import OrdemServicoCreate
from backend.app.services.ordem_servico_service import OrdemServicoService
from backend.app.database.deps import get_db

router = APIRouter(prefix="/ordens", tags=["Ordens de Serviço"])

@router.post("/")
def create(data: OrdemServicoCreate, db: Session = Depends(get_db)):
    return OrdemServicoService.create(db, data)

@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return OrdemServicoService.list_all(db)

@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    return OrdemServicoService.get_by_id(db, id)