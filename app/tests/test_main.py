import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_employee():
    response = client.post("/employees/", json={
        "name": "João Silva",
        "cpf": "12345678909",
        "rg": "12345678",
        "birth_date": "1990-01-01",
        "address": "Rua das Flores, 123",
        "marital_status": "Solteiro",
        "position": "Analista",
        "hiring_date": "2022-01-10"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "João Silva"

def test_read_employees():
    response = client.get("/employees/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_employee():
    response = client.get("/employees/1")
    assert response.status_code in [200, 404]

def test_delete_employee():
    response = client.delete("/employees/1")
    assert response.status_code in [200, 404]