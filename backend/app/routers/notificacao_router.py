from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from .auth_router import verify_token

router = APIRouter(prefix="/notificacoes", tags=["Notificacoes"])

class NotificacaoCreate(BaseModel):
    usuario_id: int
    titulo: str
    mensagem: str
    tipo: str = "INFO"
    link_referencia: Optional[str] = None

class NotificacaoResponse(NotificacaoCreate):
    id: int
    data_envio: datetime
    data_leitura: Optional[datetime] = None
    status: str

notificacoes_db = []
next_id = 1

@router.post("/", response_model=NotificacaoResponse, status_code=status.HTTP_201_CREATED)
def enviar_notificacao(data: NotificacaoCreate, _=Depends(verify_token)):
    """Enviar notificação para um usuário"""
    global next_id
    notificacao = {
        "id": next_id,
        "usuario_id": data.usuario_id,
        "titulo": data.titulo,
        "mensagem": data.mensagem,
        "tipo": data.tipo,
        "link_referencia": data.link_referencia,
        "data_envio": datetime.now(),
        "data_leitura": None,
        "status": "PENDENTE"
    }
    notificacoes_db.append(notificacao)
    next_id += 1
    return notificacao

@router.get("/", response_model=List[NotificacaoResponse])
def listar_notificacoes(_=Depends(verify_token)):
    """Listar todas as notificações"""
    return notificacoes_db

@router.patch("/{notificacao_id}/lida", response_model=NotificacaoResponse)
def marcar_notificacao_lida(notificacao_id: int, _=Depends(verify_token)):
    """Marcar notificação como lida"""
    for notificacao in notificacoes_db:
        if notificacao["id"] == notificacao_id:
            notificacao["data_leitura"] = datetime.now()
            notificacao["status"] = "LIDA"
            return notificacao
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notificação não encontrada")
