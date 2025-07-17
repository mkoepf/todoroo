from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_create_todo():
    response = client.post(
        "/todos", json={"id": 1, "title": "Test Todo", "completed": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test Todo"
    assert data["completed"] is False


def test_get_todos():
    # Should contain at least the todo created in previous test
    response = client.get("/todos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(todo["id"] == 1 for todo in data)


def test_get_todo_success():
    response = client.get("/todos/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test Todo"


def test_get_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"


def test_update_todo_success():
    response = client.put(
        "/todos/1", json={"id": 1, "title": "Updated Todo", "completed": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Todo"
    assert data["completed"] is True


def test_update_todo_not_found():
    response = client.put(
        "/todos/999",
        json={"id": 999, "title": "Doesn't exist", "completed": False},
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"


def test_delete_todo_success():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted"


def test_delete_todo_not_found():
    response = client.delete("/todos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"
