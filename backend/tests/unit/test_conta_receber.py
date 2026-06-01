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


def test_criar_conta_receber(client: TestClient):
    token = get_token(client)

    response = client.post(
        "/api/contas_receber",
        json={
            "os_id": 1,
            "cliente_id": 1,
            "valor_original": 250.0,
            "multa": 0.0,
            "juros": 0.0,
            "valor_total": 250.0,
            "data_emissao": "2026-06-01",
            "data_vencimento": "2026-06-10"
        },
        headers=auth_headers(token)
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["os_id"] == 1
    assert data["valor_total"] == 250.0
    assert data["status_pagamento"] == "PENDENTE"


def test_listar_contas_receber(client: TestClient):
    token = get_token(client)

    create_response = client.post(
        "/api/contas_receber",
        json={
            "os_id": 2,
            "cliente_id": 2,
            "valor_original": 120.0,
            "multa": 0.0,
            "juros": 0.0,
            "valor_total": 120.0,
            "data_emissao": "2026-06-01",
            "data_vencimento": "2026-06-12"
        },
        headers=auth_headers(token)
    )
    assert create_response.status_code == 201

    response = client.get(
        "/api/contas_receber",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(item["id"] == create_response.json()["id"] for item in response.json())


def test_buscar_conta_receber_por_id(client: TestClient):
    token = get_token(client)

    create_response = client.post(
        "/api/contas_receber",
        json={
            "os_id": 3,
            "cliente_id": 3,
            "valor_original": 180.0,
            "multa": 0.0,
            "juros": 0.0,
            "valor_total": 180.0,
            "data_emissao": "2026-06-01",
            "data_vencimento": "2026-06-15"
        },
        headers=auth_headers(token)
    )
    assert create_response.status_code == 201
    conta_id = create_response.json()["id"]

    response = client.get(
        f"/api/contas_receber/{conta_id}",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert response.json()["id"] == conta_id
    assert response.json()["status_pagamento"] == "PENDENTE"


def test_registrar_pagamento_conta_receber(client: TestClient):
    token = get_token(client)

    create_response = client.post(
        "/api/contas_receber",
        json={
            "os_id": 4,
            "cliente_id": 4,
            "valor_original": 300.0,
            "multa": 0.0,
            "juros": 0.0,
            "valor_total": 300.0,
            "data_emissao": "2026-06-01",
            "data_vencimento": "2026-06-20"
        },
        headers=auth_headers(token)
    )
    assert create_response.status_code == 201
    conta_id = create_response.json()["id"]

    payment_response = client.post(
        f"/api/contas_receber/{conta_id}/pagar",
        json={
            "valor_pago": 300.0,
            "forma_pagamento": "DINHEIRO",
            "transacao_id": "txn-12345"
        },
        headers=auth_headers(token)
    )

    assert payment_response.status_code == 200
    assert payment_response.json()["status_pagamento"] == "PAGO"
    assert payment_response.json()["valor_pago"] == 300.0
