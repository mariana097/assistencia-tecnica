import os
from dotenv import load_dotenv

load_dotenv()

# Caminho absoluto do projeto (raiz do backend/app/config.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Sobe 2 níveis: app -> backend -> assistencia-tecnica-ads
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DB_PATH = os.path.join(DATA_DIR, "database.sqlite")

class Config:
    # Garante URL correta mesmo em qualquer ambiente
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{os.path.abspath(DB_PATH)}"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "sua-chave-secreta-aqui-mude-em-producao"
    )

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

    PAYMENT_API_KEY = os.getenv("PAYMENT_API_KEY", "")

    APP_NAME = "Sistema de Gestão de Assistência Técnica"
    APP_VERSION = "1.0.0"

    DEBUG = os.getenv("DEBUG", "True").lower() == "true"


config = Config()