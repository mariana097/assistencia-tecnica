from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.schemas.cliente_schema import ClienteCreate, ClienteUpdate
from backend.app.services.cliente_service import ClienteService
from backend.app.database.deps import get_db

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/")
def create(data: ClienteCreate, db: Session = Depends(get_db)):
    return ClienteService.create(db, data)

@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return ClienteService.list_all(db)

@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    return ClienteService.get_by_id(db, id)

@router.put("/{id}")
def update(id: int, data: ClienteUpdate, db: Session = Depends(get_db)):
    return ClienteService.update(db, id, data)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return ClienteService.delete(db, id)