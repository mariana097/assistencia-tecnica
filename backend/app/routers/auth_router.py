from fastapi import APIRouter, HTTPException, status, Header
from pydantic import BaseModel
from typing import Optional

TOKEN = "jwt-token-758"

router = APIRouter(prefix="/auth", tags=["Autenticacao"])

class LoginRequest(BaseModel):
    email: str
    senha: str

class LoginResponse(BaseModel):
    token: str
    user: dict

# Usuário para teste
TEST_USER = {
    "email": "ricardoalsouza@gmail.com",
    "senha": "reiricardoI",
    "id": 1,
    "nome": "Ricardo",
    "tipo": "ADMIN"
}

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """Login de usuário"""
    if request.email == TEST_USER["email"] and request.senha == TEST_USER["senha"]:
        return LoginResponse(
            token=TOKEN,
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

def verify_token(authorization: Optional[str] = Header(None)):
    """Verifica token JWT via header Authorization"""
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token não fornecido")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token mal formatado")
    token = authorization.replace("Bearer ", "")
    if token != TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    return True


@router.post("/logout")
def logout():
    """Logout"""
    return {"message": "Logout realizado com sucesso"}
