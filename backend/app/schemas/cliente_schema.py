from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime
from typing import Optional

class ClienteBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    endereco: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None

class ClienteResponse(ClienteBase):
    id: int
    data_cadastro: datetime
    ativo: bool
    
    model_config = ConfigDict(from_attributes=True)
