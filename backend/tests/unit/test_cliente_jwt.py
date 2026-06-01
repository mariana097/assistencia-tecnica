import pytest
from fastapi.testclient import TestClient


def get_token(client: TestClient) -> str:
    response = client.post(
        "/api/auth/login",
        json={
            "email": "admin@assistencia.com",
            "senha": "admin123"
        }
    )
    assert response.status_code == 200
    return response.json()["token"]


def auth_headers(token: str):
    return {"Authorization": f"Bearer {token}"}


def test_cliente_jwt_protected_route(client: TestClient):
    token = get_token(client)

    response = client.get(
        "/api/clientes/",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
