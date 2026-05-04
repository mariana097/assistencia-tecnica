# Configurações do sistema
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class Config:
    # Banco de dados
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///../data/database.sqlite")
    
    # Segurança
    SECRET_KEY = os.getenv("SECRET_KEY", "sua-chave-secreta-aqui-mude-em-producao")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 horas
    
    # Gateway de Pagamento (futuro)
    PAYMENT_API_KEY = os.getenv("PAYMENT_API_KEY", "")
    
    # Configurações do sistema
    APP_NAME = "Sistema de Gestão de Assistência Técnica"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "True") == "True"

config = Config()
