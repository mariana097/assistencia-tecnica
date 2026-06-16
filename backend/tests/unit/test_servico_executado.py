import pytest
from datetime import datetime
from backend.app.models.funcionario import Funcionario


class TestServicoExecutado:
    def setup_method(self):
        self.tecnico = Funcionario(
            id=10,
            nome="Técnico Teste",
            email="tecnico.teste@assistencia.com",
            cpf="98765432100",
            telefone="11988887777",
            cargo="TECNICO",
            salario=4200.00,
            especialidade="Informática",
            nivel_experiencia=4,
            comissao_percentual=15.0
        )

    def test_iniciar_servico_executado(self):
        resultado = self.tecnico.iniciar_execucao_servico(101)

        assert resultado["servico_executado_id"] == 101
        assert resultado["tecnico_id"] == self.tecnico.id
        assert resultado["status"] == "EM_EXECUCAO"
        assert isinstance(resultado["data_inicio"], datetime)

    def test_finalizar_servico_executado(self):
        resultado = self.tecnico.finalizar_execucao_servico(101, 2.75)

        assert resultado["servico_executado_id"] == 101
        assert resultado["tecnico_id"] == self.tecnico.id
        assert resultado["status"] == "CONCLUIDO"
        assert resultado["tempo_gasto"] == 2.75
        assert isinstance(resultado["data_fim"], datetime)
