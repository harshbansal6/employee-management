from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_token(username: str, password: str):
    response = client.post("/api/login", data={
        "grant_type": "password",
        "username": username,
        "password": password,
        "scope": "",
        "client_id": "",
        "client_secret": ""
    })
    print(response.json())
    assert response.status_code == 200
    return response.json()["access_token"]

def test_create_employee():
    token = get_token("abc", "testdemo")  # Replace with your actual test credentials
    response = client.post(
        f"/api/employees?token={token}",  # Include token as a query parameter
        json={
            "name": "alex",
            "email": "alex@gmail.com",
            "department": "HR",
            "role": "HR Manager"
        },
        headers={"accept": "application/json", "Content-Type": "application/json"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "alex"

# Example for other test cases if needed
def test_get_employee():
    token = get_token("abc", "testdemo")  # Replace with your actual test credentials
    response = client.get(f"/api/employees/5?token={token}")  # Include token in the URL
    assert response.status_code == 200
    assert response.json()["name"] == "alex"

def test_update_employee():
    token = get_token("abc", "testdemo")  # Replace with your actual test credentials
    response = client.put(
        f"/api/employees/5?token={token}",  # Include token in the URL
        json={"name": "Jane Doe"},
        headers={"accept": "application/json", "Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_delete_employee():
    token = get_token("abc", "testdemo")  # Replace with your actual test credentials
    response = client.delete(f"/api/employees/5?token={token}")  # Include token in the URL
    assert response.status_code == 204
    response = client.get(f"/api/employees/3?token={token}")  # Include token in the URL
    assert response.status_code == 404