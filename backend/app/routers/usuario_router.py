from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    tipo: str = "CLIENTE"

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    status: str

# Dados em memória
usuarios_db = []
next_id = 1

@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios():
    """Listar todos os usuários"""
    return usuarios_db

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar_usuario(data: UsuarioCreate):
    """Criar novo usuário"""
    global next_id
    
    # Verificar email duplicado
    for u in usuarios_db:
        if u["email"] == data.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email já cadastrado"
            )
    
    usuario = {
        "id": next_id,
        "nome": data.nome,
        "email": data.email,
        "status": "ATIVO"
    }
    usuarios_db.append(usuario)
    next_id += 1
    return usuario

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def buscar_usuario(usuario_id: int):
    """Buscar usuário por ID"""
    for u in usuarios_db:
        if u["id"] == usuario_id:
            return u
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuário não encontrado"
    )

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def atualizar_usuario(usuario_id: int, data: dict):
    """Atualizar usuário"""
    for i, u in enumerate(usuarios_db):
        if u["id"] == usuario_id:
            usuarios_db[i].update(data)
            return usuarios_db[i]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuário não encontrado"
    )

@router.delete("/{usuario_id}")
def desativar_usuario(usuario_id: int):
    """Desativar usuário"""
    for i, u in enumerate(usuarios_db):
        if u["id"] == usuario_id:
            usuarios_db[i]["status"] = "INATIVO"
            return {"message": "Usuário desativado com sucesso"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuário não encontrado"
    )
