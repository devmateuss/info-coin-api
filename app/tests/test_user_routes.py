import pytest
from unittest.mock import patch


@pytest.fixture
def new_user_data():
    return {
        "username": "newuser",
        "password": "newpassword",
        "email": "newuser@example.com"
    }

@pytest.fixture
def existing_user_data():
    return {
        "username": "existinguser",
        "password": "password123",
        "email": "existinguser@example.com"
    }

def test_create_user_success(client, new_user_data, app):
    with patch('app.routes.user_routes.UserService.create_user') as mock_create_user:
        mock_create_user.return_value = {"id": 1, "username": "newuser"}, 201

        response = client.post('/api/users/create', json=new_user_data)

        assert response.status_code == 201
        data = response.get_json()
        assert "id" in data
        assert data["username"] == "newuser"

def test_create_user_already_exists(client, existing_user_data, app):
    with patch('app.routes.user_routes.UserService.create_user') as mock_create_user:
        mock_create_user.return_value = {"error": "User already exists"}, 400

        response = client.post('/api/users/create', json=existing_user_data)

        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert data["error"] == "User already exists"


def test_create_user_missing_fields(client, app):
    incomplete_data = {"username": "incompleteuser"}
    
    with patch('app.routes.user_routes.UserService.create_user') as mock_create_user:
        mock_create_user.return_value = {"error": "Username and password are required"}, 400

        response = client.post('/api/users/create', json=incomplete_data)

        assert response.status_code == 400
        data = response.get_json()
        assert "error" in data
        assert data["error"] == "Username and password are required"


def test_create_user_invalid_json(client, app):
    invalid_data = {
        "user": "teste1",
        "pass": "teste1"
    }
    
    response = client.post('/api/users/create', data=invalid_data, content_type='application/json')

    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_create_user_internal_error(client, new_user_data, app):
    with patch('app.routes.user_routes.UserService.create_user') as mock_create_user:
        mock_create_user.side_effect = Exception("Unexpected error")

        response = client.post('/api/users/create', json=new_user_data)

        assert response.status_code == 500
        data = response.get_json()
        assert "error" in data
        assert data["error"] == "Unexpected error"
