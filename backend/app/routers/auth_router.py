from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.schemas.auth_schema import LoginSchema
from backend.app.services.auth_service import AuthService
from backend.app.database.deps import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    token = AuthService.login(db, data.email, data.senha)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"access_token": token}