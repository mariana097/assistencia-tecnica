import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///../data/database.sqlite")
    SECRET_KEY = os.getenv("SECRET_KEY", "chave-secreta-dev")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

config = Config()
