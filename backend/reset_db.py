from app.database import engine, Base
from app.models import usuario
from app.models.cliente import Cliente
from app.models.funcionario import Funcionario

print("Removendo tabelas existentes...")
Base.metadata.drop_all(bind=engine)

print("Criando novas tabelas...")
Base.metadata.create_all(bind=engine)

print("✅ Banco de dados recriado com sucesso!")
