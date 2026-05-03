from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Cliente, Usuario
from ..schemas import ClienteCreate, ClienteResponse, ClienteUpdate
from ..routers.auth_router import oauth2_scheme
from ..utils import decodificar_token

router = APIRouter()

# Função para obter usuário atual a partir do token
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decodificar_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    email = payload.get("sub")
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return email

# Rota para criar cliente
@router.post("/", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def create_cliente(cliente_data: ClienteCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """
    Cria um novo cliente no sistema.
    """
    # Verificar se o cliente já existe (por nome e usuário)
    cliente_existente = db.query(Cliente).filter(
        Cliente.nome == cliente_data.nome,
        Cliente.usuario_id == cliente_data.usuario_id
    ).first()
    if cliente_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cliente já cadastrado para este usuário"
        )

    # Criar novo cliente
    novo_cliente = Cliente(
        nome=cliente_data.nome,
        endereco=cliente_data.endereco,
        contato=cliente_data.contato,
        tipo=cliente_data.tipo,
        usuario_id=cliente_data.usuario_id
    )

    # Adicionar dados específicos para PF se fornecidos
    if cliente_data.pf_data:
        novo_cliente.cpf = cliente_data.pf_data.cpf
        novo_cliente.data_nascimento = cliente_data.pf_data.data_nascimento

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return novo_cliente

# Rota para listar clientes do usuário atual
@router.get("/", response_model=List[ClienteResponse])
def get_clientes(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """
    Lista todos os clientes do usuário autenticado.
    """
    clientes = db.query(Cliente).join(Usuario).filter(Usuario.email == current_user).all()
    return clientes

# Rota para obter cliente por ID
@router.get("/{cliente_id}", response_model=ClienteResponse)
def get_cliente(cliente_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """
    Obtém um cliente específico por ID.
    """
    cliente = db.query(Cliente).join(Usuario).filter(
        Cliente.id == cliente_id,
        Usuario.email == current_user
    ).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    return cliente

# Rota para atualizar cliente
@router.put("/{cliente_id}", response_model=ClienteResponse)
def update_cliente(cliente_id: int, cliente_data: ClienteUpdate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """
    Atualiza os dados de um cliente.
    """
    cliente = db.query(Cliente).join(Usuario).filter(
        Cliente.id == cliente_id,
        Usuario.email == current_user
    ).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    # Atualizar campos fornecidos
    update_data = cliente_data.dict(exclude_unset=True)
    pf_data = update_data.pop('pf_data', None)

    for field, value in update_data.items():
        setattr(cliente, field, value)

    # Atualizar dados PF se fornecidos
    if pf_data:
        cliente.cpf = pf_data.get('cpf', cliente.cpf)
        cliente.data_nascimento = pf_data.get('data_nascimento', cliente.data_nascimento)

    db.commit()
    db.refresh(cliente)
    return cliente

# Rota para buscar cliente por CPF
@router.get("/buscar/{cpf}", response_model=ClienteResponse)
def buscar_cliente_por_cpf(cpf: str, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    """
    Busca um cliente pelo CPF.
    """
    cliente = db.query(Cliente).join(Usuario).filter(
        Cliente.cpf == cpf,
        Usuario.email == current_user
    ).first()
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado com este CPF"
        )
    return cliente