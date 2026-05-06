from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from .config import config

# Diretório base do projeto (app/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Garante caminho absoluto do SQLite
if config.DATABASE_URL.startswith("sqlite"):
    DB_PATH = os.path.join(BASE_DIR, "..", "..", "data", "database.sqlite")
    DATABASE_URL = f"sqlite:///{os.path.abspath(DB_PATH)}"
else:
    DATABASE_URL = config.DATABASE_URL

# Engine do banco
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # necessário só para SQLite
)

# Sessão
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base dos modelos
Base = declarative_base()

# Dependência do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()