
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def load_sample():
    client.post("/load-sample-data")

def test_search_basic_query():
    response = client.get("/search?org_id=1&q=alice")
    assert response.status_code == 200
    results = response.json()
    assert any("Alice" in emp.get("name", "") for emp in results)

def test_search_with_filters():
    response = client.get("/search?org_id=1&location=NY&status=Active")
    assert response.status_code == 200
    assert all(emp.get("location") == "NY" and emp.get("status") == "Active" for emp in response.json())

def test_search_by_status():
    response = client.get("/search?org_id=1&status=Not%20Started")
    assert response.status_code == 200
    assert all(emp.get("status") == "Not Started" for emp in response.json())

def test_search_pagination():
    response = client.get("/search?org_id=1&page=1&page_size=1")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_search_invalid_org_no_data_leak():
    response = client.get("/search?org_id=999")
    assert response.status_code == 200
    assert response.json() == []

def test_rate_limit_exceeded():
    for _ in range(10):
        client.get("/search?org_id=1")
    response = client.get("/search?org_id=1")
    assert response.status_code == 429
    assert response.json()["detail"] == "Rate limit exceeded"
