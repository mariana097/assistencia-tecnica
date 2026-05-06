import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

# =========================
# 🔐 TOKEN
# =========================
def get_token():
    response = client.post(
        "/api/auth/login",
        json={
            "email": "jadsonhipolito@gmail.com",
            "senha": "Testando123"
        }
    )

    assert response.status_code == 200
    return response.json()["access_token"]


# =========================
# 🔐 AUTH FAIL
# =========================
def test_login_falha():
    response = client.post(
        "/api/auth/login",
        json={
            "email": "errado@teste.com",
            "senha": "errada"
        }
    )

    assert response.status_code in (400, 401)


def test_token_invalido():
    response = client.get(
        "/api/funcionarios/",
        headers={"Authorization": "Bearer TOKEN_INVALIDO"}
    )

    assert response.status_code == 401


def test_sem_token():
    response = client.get("/api/funcionarios/")
    assert response.status_code == 401


# =========================
# 🧱 CREATE FUNCIONARIO
# =========================
def test_criar_funcionario_valido():
    token = get_token()

    response = client.post(
        "/api/funcionarios/",
        json={
            "nome": "Teste",
            "endereco": "Rua X",
            "contato": "999",
            "usuario_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["nome"] == "Teste"


def test_criar_funcionario_payload_invalido():
    token = get_token()

    response = client.post(
        "/api/funcionarios/",
        json={},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 422


def test_criar_funcionario_dados_maliciosos():
    token = get_token()

    response = client.post(
        "/api/funcionarios/",
        json={
            "nome": "'; DROP TABLE --",
            "endereco": "<script>alert(1)</script>",
            "contato": "999",
            "usuario_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code in (200, 400, 422)


# =========================
# 📄 LISTAGEM
# =========================
def test_listar_funcionarios():
    token = get_token()

    response = client.get(
        "/api/funcionarios/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# =========================
# 🔎 CONSULTA
# =========================
def test_funcionario_inexistente():
    token = get_token()

    response = client.get(
        "/api/funcionarios/999999",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404


# =========================
# 🌐 ROTAS
# =========================
def test_rota_inexistente():
    token = get_token()

    response = client.get(
        "/api/funcionarios/rota-que-nao-existe",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404


# =========================
# 🔐 HEADER INVÁLIDO
# =========================
def test_header_mal_formado():
    token = get_token()

    response = client.get(
        "/api/funcionarios/",
        headers={"Authorization": token}  # sem Bearer
    )

    assert response.status_code == 401