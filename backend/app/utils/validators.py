import re

def validar_email(email: str) -> bool:
    """Valida formato de email"""
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email) is not None

def validar_senha(senha: str) -> tuple[bool, str]:
    """Valida força da senha"""
    if len(senha) < 6:
        return False, "A senha deve ter no mínimo 6 caracteres"
    return True, "OK"