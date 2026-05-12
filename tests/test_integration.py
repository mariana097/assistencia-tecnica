import pytest


class TestIntegration:
    """Testes de integração do sistema"""

    def test_health_check(self, client):
        """Testa endpoint de saúde"""
        response = client.get("/health")
        assert response.status_code == 200

        data = response.json()
        assert data.get("status") == "ok"

    def test_root_endpoint(self, client):
        """Testa endpoint raiz"""
        response = client.get("/")
        assert response.status_code == 200
        assert "message" in response.json()

    def test_documentacao_disponivel(self, client):
        """Testa se a documentação está disponível"""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_cors_headers(self, client):
        """Testa se os headers CORS estão configurados"""
        origin = "http://localhost:3000"

        response = client.get(
            "/",
            headers={"Origin": origin}
        )

        assert response.status_code == 200
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == origin