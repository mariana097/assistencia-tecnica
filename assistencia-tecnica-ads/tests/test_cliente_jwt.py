import pytest
from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)

# =========================
# 🔐 TOKEN JWT (JWS)
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
    data = response.json()

    assert "access_token" in data
    return data["access_token"]


def auth_headers(token: str):
    return {"Authorization": f"Bearer {token}"}


# =========================
# 🚨 SEGURANÇA JWT
# =========================
def test_acesso_sem_token():
    response = client.get("/api/clientes/")
    assert response.status_code == 401


def test_token_invalido():
    response = client.get(
        "/api/clientes/",
        headers={"Authorization": "Bearer token_invalido_123"}
    )
    assert response.status_code == 401


def test_header_mal_formado():
    token = get_token()

    response = client.get(
        "/api/clientes/",
        headers={"Authorization": token}  # sem Bearer
    )

    assert response.status_code == 401


# =========================
# 🧪 CREATE CLIENTE
# =========================
def test_criar_cliente():
    token = get_token()

    response = client.post(
        "/api/clientes/",
        json={
            "nome": "Cliente Teste",
            "endereco": "Rua X, 123",
            "contato": "99999-9999"
        },
        headers=auth_headers(token)
    )

    assert response.status_code == 200

    data = response.json()
    assert data["nome"] == "Cliente Teste"


def test_criar_cliente_payload_vazio():
    token = get_token()

    response = client.post(
        "/api/clientes/",
        json={},
        headers=auth_headers(token)
    )

    assert response.status_code == 422


# =========================
# 🧪 LISTAR CLIENTES
# =========================
def test_listar_clientes():
    token = get_token()

    response = client.get(
        "/api/clientes/",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# =========================
# 🧪 BUSCAR CLIENTE
# =========================
def test_buscar_cliente_inexistente():
    token = get_token()

    response = client.get(
        "/api/clientes/999999",
        headers=auth_headers(token)
    )

    assert response.status_code == 404


# =========================
# 🧪 UPDATE CLIENTE
# =========================
def test_atualizar_cliente():
    token = get_token()

    # cria cliente primeiro
    create = client.post(
        "/api/clientes/",
        json={
            "nome": "Update Test",
            "endereco": "Rua A",
            "contato": "11111"
        },
        headers=auth_headers(token)
    )

    cliente_id = create.json()["id"]

    # atualiza
    response = client.put(
        f"/api/clientes/{cliente_id}",
        json={
            "nome": "Atualizado",
            "endereco": "Rua B",
            "contato": "22222"
        },
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert response.json()["nome"] == "Atualizado"


# =========================
# 🧪 DELETE CLIENTE
# =========================
def test_deletar_cliente():
    token = get_token()

    create = client.post(
        "/api/clientes/",
        json={
            "nome": "Delete Test",
            "endereco": "Rua Z",
            "contato": "33333"
        },
        headers=auth_headers(token)
    )

    cliente_id = create.json()["id"]

    response = client.delete(
        f"/api/clientes/{cliente_id}",
        headers=auth_headers(token)
    )

    assert response.status_code == 200


# =========================
# 🚨 ROTAS INEXISTENTES (JWS + ROTEAMENTO)
# =========================
def test_rota_inexistente():
    token = get_token()

    response = client.get(
        "/api/clientes/rota-que-nao-existe",
        headers=auth_headers(token)
    )

    # pode variar dependendo do FastAPI + router
    assert response.status_code in [404, 422]