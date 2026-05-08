import pytest

class TestIntegration:
    """Testes de integração do sistema"""

    def test_health_check(self, client):
        """Testa endpoint de saúde"""
        response = client.get("/health")
        assert response.status_code == 200
        # Aceita resposta com ou sem message
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
        response = client.get("/")
        assert "access-control-allow-origin" in response.headers
