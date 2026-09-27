from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_companies_listing():
    response = client.get("/api/v1/companies?q=اتصالات")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert data["total"] >= 1


def test_suggestions():
    response = client.get("/api/v1/search/suggestions?q=اتص")
    assert response.status_code == 200
    assert "items" in response.json()


def test_normalization():
    from app.services.normalization import normalize_arabic
    assert normalize_arabic("شركة الإتصالات السعودية") == "شركة الاتصالات السعودية"
    assert normalize_arabic("شركة  الاتصالات   السعودية") == "شركة الاتصالات السعودية"
