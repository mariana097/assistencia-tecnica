import pytest

from backend.app.models.usuario import Usuario
from backend.app.models.funcionario import Funcionario


def test_usuario_autenticar_alterar_senha_e_status():
    usuario = Usuario(email="bryan@gmail.com", senha="senha123", nome="Teste")

    assert usuario.autenticar("senha123") is True
    assert usuario.autenticar("senha_errada") is False

    assert usuario.alterar_senha("nova123") is True
    assert usuario.senha == "nova123"

    usuario.desativar()
    assert usuario.status == "INATIVO"

    usuario.ativar()
    assert usuario.status == "ATIVO"


def test_usuario_alterar_senha_curta_gera_erro():
    usuario = Usuario(email="bryan@gmail.com", senha="senha123", nome="Teste")

    with pytest.raises(ValueError, match="Senha deve ter no mínimo 6 caracteres"):
        usuario.alterar_senha("123")


def test_funcionario_validacao_de_experiencia_e_comissao():
    with pytest.raises(ValueError, match="Nível de experiência deve ser entre 1 e 5"):
        Funcionario(
            nome="Técnico",
            email="arthur@gmail.com",
            cargo="TECNICO",
            telefone="11999999999",
            salario=3000.0,
            cpf="12345678900",
            senha="senha123",
            nivel_experiencia=0,
            comissao_percentual=5.0
        )

    with pytest.raises(ValueError, match="Comissão deve ser entre 0% e 30%"):
        Funcionario(
            nome="Técnico",
            email="arthur@gmail.com",
            cargo="TECNICO",
            telefone="11999999999",
            salario=3000.0,
            cpf="12345678900",
            senha="senha123",
            nivel_experiencia=3,
            comissao_percentual=40.0
        )


def test_funcionario_calcular_comissao():
    funcionario = Funcionario(
        nome="Técnico",
        email="arthur@gmail.com",
        cargo="TECNICO",
        telefone="11999999999",
        salario=3000.0,
        cpf="12345678900",
        senha="senha123",
        nivel_experiencia=3,
        comissao_percentual=10.0
    )

    assert funcionario.calcular_comissao(100.0) == 10.0
