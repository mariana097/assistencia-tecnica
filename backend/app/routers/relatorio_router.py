from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models.cliente import Cliente
from app.models.funcionario import Funcionario
from app.models.usuario import Usuario

router = APIRouter(prefix="/relatorios", tags=["Relatórios"])

@router.get("/dashboard/resumo")
def dashboard_resumo(db: Session = Depends(get_db)):
    total_clientes = db.query(Cliente).count()
    total_usuarios = db.query(Usuario).count()
    total_funcionarios = db.query(Funcionario).count()
    
    return {
        "resumo": {
            "total_clientes": total_clientes,
            "total_usuarios": total_usuarios,
            "total_funcionarios": total_funcionarios
        },
        "gerado_em": datetime.now().isoformat()
    }

@router.get("/usuarios")
def relatorio_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    
    return {
        "tipo": "usuarios",
        "total": len(usuarios),
        "usuarios": [
            {
                "id": u.id,
                "nome": u.nome,
                "email": u.email,
                "tipo": u.tipo
            } for u in usuarios
        ],
        "gerado_em": datetime.now().isoformat()
    }

@router.get("/clientes")
def relatorio_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    
    return {
        "tipo": "clientes",
        "total": len(clientes),
        "clientes": [
            {
                "id": c.id,
                "nome": c.nome,
                "email": c.email,
                "telefone": c.telefone
            } for c in clientes
        ],
        "gerado_em": datetime.now().isoformat()
    }

@router.get("/funcionarios")
def relatorio_funcionarios(db: Session = Depends(get_db)):
    funcionarios = db.query(Funcionario).all()
    
    return {
        "tipo": "funcionarios",
        "total": len(funcionarios),
        "funcionarios": [
            {
                "id": f.id,
                "nome": f.nome,
                "email": f.email,
                "cargo": f.cargo,
                "telefone": f.telefone
            } for f in funcionarios
        ],
        "gerado_em": datetime.now().isoformat()
    }

@router.get("/completo")
def relatorio_completo(db: Session = Depends(get_db)):
    total_clientes = db.query(Cliente).count()
    total_usuarios = db.query(Usuario).count()
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
