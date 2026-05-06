from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timedelta
import json

from app.database import get_db
from app.models.cliente import Cliente
from app.models.funcionario import Funcionario
from app.models.usuario import Usuario

router = APIRouter(prefix="/relatorios", tags=["Relatórios"])

@router.get("/dashboard/resumo")
def dashboard_resumo(db: Session = Depends(get_db)):
    """Dashboard com resumo do sistema"""
    
    total_clientes = db.query(Cliente).count()
    total_usuarios = db.query(Usuario).filter(Usuario.ativo == True).count()
    total_funcionarios = db.query(Funcionario).count()
    
    # Últimos clientes cadastrados
    ultimos_clientes = db.query(Cliente).order_by(Cliente.id.desc()).limit(5).all()
    
    return {
        "resumo": {
            "total_clientes": total_clientes,
            "total_usuarios": total_usuarios,
            "total_funcionarios": total_funcionarios
        },
        "ultimos_clientes": [
            {
                "id": c.id,
                "nome": c.nome,
                "email": c.email,
                "data_cadastro": c.data_cadastro.isoformat() if hasattr(c, 'data_cadastro') else None
            } for c in ultimos_clientes
        ],
        "gerado_em": datetime.now().isoformat()
    }

@router.get("/clientes")
def relatorio_clientes(
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Relatório de clientes"""
    
    query = db.query(Cliente)
    
    # Aplicar filtros de data se necessário
    # (Assumindo que existe campo data_cadastro)
    
    clientes = query.all()
    
    return {
        "tipo": "clientes",
        "total": len(clientes),
        "clientes": [
            {
                "id": c.id,
                "nome": c.nome,
                "email": c.email,
                "telefone": getattr(c, 'telefone', 'N/A')
            } for c in clientes
        ],
        "gerado_em": datetime.now().isoformat()
    }

@router.get("/funcionarios")
def relatorio_funcionarios(db: Session = Depends(get_db)):
    """Relatório de funcionários"""
    
    funcionarios = db.query(Funcionario).all()
    
    return {
        "tipo": "funcionarios",
        "total": len(funcionarios),
        "funcionarios": [
            {
                "id": f.id,
                "nome": f.nome,
                "cargo": getattr(f, 'cargo', 'N/A'),
                "telefone": getattr(f, 'telefone', 'N/A')
            } for f in funcionarios
        ],
        "gerado_em": datetime.now().isoformat()
    }

@router.get("/usuarios")
def relatorio_usuarios(db: Session = Depends(get_db)):
    """Relatório de usuários"""
    
    usuarios = db.query(Usuario).filter(Usuario.ativo == True).all()
    
    return {
        "tipo": "usuarios",
        "total": len(usuarios),
        "usuarios": [
            {
                "id": u.id,
                "nome": u.nome,
                "email": u.email,
                "tipo": u.tipo,
                "criado_em": u.created_at.isoformat() if u.created_at else None
            } for u in usuarios
        ],
        "gerado_em": datetime.now().isoformat()
    }

@router.get("/completo")
def relatorio_completo(db: Session = Depends(get_db)):
    """Relatório completo do sistema"""
    
    total_clientes = db.query(Cliente).count()
    total_usuarios = db.query(Usuario).filter(Usuario.ativo == True).count()
    total_funcionarios = db.query(Funcionario).count()
    
    return {
        "resumo_geral": {
            "clientes": total_clientes,
            "usuarios": total_usuarios,
            "funcionarios": total_funcionarios,
            "total_geral": total_clientes + total_usuarios + total_funcionarios
        },
        "gerado_em": datetime.now().isoformat()
    }
