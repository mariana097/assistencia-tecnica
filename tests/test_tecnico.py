import pytest
from app.models.tecnico import Tecnico

class TestTecnicoModel:
    """Testes para o modelo Tecnico"""

    def setup_method(self):
        self.tecnico = Tecnico(
            id=1,
            nome="Carlos Tecnico",
            email="carlos@empresa.com",
            cpf="12345678900",
            telefone="11999999999",
            cargo="TECNICO",
            salario=3500.00,
            especialidade="Eletrônica",
            nivel_experiencia=3,
            comissao_percentual=10.0
        )

    def test_criar_tecnico(self):
        assert self.tecnico.especialidade == "Eletrônica"
        assert self.tecnico.nivel_experiencia == 3
        assert self.tecnico.comissao_percentual == 10.0

    def test_nivel_experiencia_invalido(self):
        with pytest.raises(ValueError):
            Tecnico(
                id=2,
                nome="Teste",
                email="teste@email.com",
                cpf="12345678900",
                telefone="11999999999",
                cargo="TECNICO",
                salario=3500.00,
                especialidade="Informática",
                nivel_experiencia=6,
                comissao_percentual=10.0
            )

    def test_comissao_invalida(self):
        with pytest.raises(ValueError):
            Tecnico(
                id=2,
                nome="Teste",
                email="teste@email.com",
                cpf="12345678900",
                telefone="11999999999",
                cargo="TECNICO",
                salario=3500.00,
                especialidade="Informática",
                nivel_experiencia=3,
                comissao_percentual=50.0
            )

    def test_calcular_comissao(self):
        comissao = self.tecnico.calcular_comissao(1000.00)
        assert comissao == 100.00

    def test_iniciar_execucao_servico(self):
        result = self.tecnico.iniciar_execucao_servico(1)
        assert result["servico_executado_id"] == 1
        assert result["tecnico_id"] == self.tecnico.id
        assert "data_inicio" in result

    def test_finalizar_execucao_servico(self):
        result = self.tecnico.finalizar_execucao_servico(1, 2.5)
        assert result["status"] == "CONCLUIDO"
        assert result["tempo_gasto"] == 2.5
