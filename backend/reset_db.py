from backend.app.database import engine, Base
from backend.app.models import usuario
from backend.app.models.cliente import Cliente
from backend.app.models.funcionario import Funcionario
from backend.app.models.ordem_servico import OrdemServico
from backend.app.models.servico_executado import ServicoExecutado
from backend.app.models.equipamento_usado import EquipamentoUsado
from backend.app.models.conta_receber import ContaReceber
from backend.app.models.notificacao import Notificacao

print("Removendo tabelas existentes...")
Base.metadata.drop_all(bind=engine)

print("Criando novas tabelas...")
Base.metadata.create_all(bind=engine)

print("✅ Banco de dados recriado com sucesso!")
