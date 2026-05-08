from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/funcionarios", tags=["Funcionarios"])

class FuncionarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    cpf: str
    contato: str
    salario: float
    cargo: str

class FuncionarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    cpf: str
    cargo: str
    status: str

# Dados em memória
funcionarios_db = []
next_id = 1

@router.get("/", response_model=List[FuncionarioResponse])
def listar_funcionarios():
    """Listar todos os funcionários"""
    return funcionarios_db

@router.post("/", response_model=FuncionarioResponse, status_code=status.HTTP_201_CREATED)
def criar_funcionario(data: FuncionarioCreate):
    """Criar novo funcionário"""
    global next_id
    
    funcionario = {
        "id": next_id,
        "nome": data.nome,
        "email": data.email,
        "cpf": data.cpf,
        "cargo": data.cargo,
        "status": "ATIVO"
    }
    funcionarios_db.append(funcionario)
    next_id += 1
    return funcionario

@router.get("/{funcionario_id}", response_model=FuncionarioResponse)
def buscar_funcionario(funcionario_id: int):
    """Buscar funcionário por ID"""
    for f in funcionarios_db:
        if f["id"] == funcionario_id:
            return f
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Funcionário não encontrado"
    )

@router.delete("/{funcionario_id}")
def desativar_funcionario(funcionario_id: int):
    """Desativar funcionário"""
    for i, f in enumerate(funcionarios_db):
        if f["id"] == funcionario_id:
            funcionarios_db[i]["status"] = "INATIVO"
            return {"message": "Funcionário desativado com sucesso"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Funcionário não encontrado"
    )
