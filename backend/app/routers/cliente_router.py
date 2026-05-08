from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/api/clientes", tags=["Clientes"])

class ClienteCreate(BaseModel):
    nome: str
    email: str
    telefone: str

class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

# Dados em memória
clientes_db = []
next_id = 1

def verify_token(authorization: Optional[str] = Header(None)):
    """Verificar token JWT"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Token não fornecido")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token mal formatado")
    token = authorization.replace("Bearer ", "")
    if token != "fake-jwt-token-123":
        raise HTTPException(status_code=401, detail="Token inválido")
    return True

@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(_=Depends(verify_token)):
    """Listar todos os clientes"""
    return clientes_db

@router.post("/", response_model=ClienteResponse, status_code=201)
def criar_cliente(data: ClienteCreate, _=Depends(verify_token)):
    """Criar novo cliente"""
    global next_id
    cliente = {
        "id": next_id,
        "nome": data.nome,
        "email": data.email,
        "telefone": data.telefone
    }
    clientes_db.append(cliente)
    next_id += 1
    return cliente

@router.get("/{cliente_id}", response_model=ClienteResponse)
def buscar_cliente(cliente_id: int, _=Depends(verify_token)):
    """Buscar cliente por ID"""
    for c in clientes_db:
        if c["id"] == cliente_id:
            return c
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@router.put("/{cliente_id}", response_model=ClienteResponse)
def atualizar_cliente(cliente_id: int, data: ClienteCreate, _=Depends(verify_token)):
    """Atualizar cliente"""
    for i, c in enumerate(clientes_db):
        if c["id"] == cliente_id:
            clientes_db[i] = {**c, **data.dict()}
            return clientes_db[i]
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: int, _=Depends(verify_token)):
    """Deletar cliente"""
    for i, c in enumerate(clientes_db):
        if c["id"] == cliente_id:
            del clientes_db[i]
            return {"message": "Cliente deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado")
