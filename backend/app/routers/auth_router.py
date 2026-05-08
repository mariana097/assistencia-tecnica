from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/auth", tags=["Autenticacao"])

class LoginRequest(BaseModel):
    email: str
    senha: str

class LoginResponse(BaseModel):
    token: str
    user: dict

# Usuário para teste
TEST_USER = {
    "email": "admin@assistencia.com",
    "senha": "admin123",
    "id": 1,
    "nome": "Admin",
    "tipo": "ADMIN"
}

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """Login de usuário"""
    if request.email == TEST_USER["email"] and request.senha == TEST_USER["senha"]:
        return LoginResponse(
            token="fake-jwt-token-123",
            user={"id": TEST_USER["id"], "email": TEST_USER["email"], "nome": TEST_USER["nome"]}
        )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas"
    )

@router.post("/recuperar-senha")
def recuperar_senha(email: dict):
    """Recuperar senha"""
    return {"message": "Email enviado"}

@router.post("/logout")
def logout():
    """Logout"""
    return {"message": "Logout realizado com sucesso"}
