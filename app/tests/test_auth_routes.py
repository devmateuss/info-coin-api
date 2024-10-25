import pytest
from unittest.mock import patch, MagicMock
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "testpassword"
    }

def test_auth_login_route(client, user_data, app):
    fake_token = "fake_jwt_token"

    with patch('app.routes.auth_routes.AuthenticationService.login') as mock_login:
        mock_login.return_value = {"access_token": fake_token}, 200

        response = client.post('/api/auth/login', json=user_data)

        assert response.status_code == 200
        data = response.get_json()
        assert "access_token" in data
        assert data["access_token"] == fake_token

def test_auth_login_failure(client, user_data, app):
    error_message = "Invalid credentials"

    with patch('app.routes.auth_routes.AuthenticationService.login') as mock_login:
        mock_login.return_value = {"error": error_message}, 401

        response = client.post('/api/auth/login', json=user_data)

        assert response.status_code == 401
        data = response.get_json()
        assert "error" in data
        assert data["error"] == error_message
