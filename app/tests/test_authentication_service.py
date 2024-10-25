import pytest
from unittest.mock import MagicMock

def test_login_successful(auth_service, mock_db, mocker, app):
    request_data = {
        "username": "testuser",
        "password": "password123"
    }
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.password = auth_service.hash_password(request_data["password"])
    
    mocker.patch('app.repositories.user_repository.UserRepository.get_user_by_username', return_value=mock_user)
    
    with app.test_request_context(json=request_data):
        mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))

        result_data, result_status = auth_service.login(mock_response)
    
        assert result_status == 200
        assert "access_token" in result_data.get_json()

def test_login_missing_username(auth_service, mock_db, mocker, app):
    request_data = {
        "password": "password123"
    }

    with app.test_request_context(json=request_data):
        mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))

        result_data, result_status = auth_service.login(mock_response)

        assert result_status == 400
        assert result_data.get_json() == {"error": "Username and password are required"}


def test_login_missing_password(auth_service, mock_db, mocker, app):
    request_data = {
        "username": "testuser"
    }

    with app.test_request_context(json=request_data):
        mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))

        result_data, result_status = auth_service.login(mock_response)

        assert result_status == 400
        assert result_data.get_json() == {"error": "Username and password are required"}

def test_login_invalid_credentials(auth_service, mock_db, mocker, app):
    request_data = {
        "username": "testuser",
        "password": "wrongpassword"
    }
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.password = auth_service.hash_password("correctpassword")

    mocker.patch('app.repositories.user_repository.UserRepository.get_user_by_username', return_value=mock_user)

    with app.test_request_context(json=request_data):
        mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))

        result_data, result_status = auth_service.login(mock_response)

        assert result_status == 401
        assert result_data.get_json() == {"error": "Invalid credentials"}

def test_login_user_not_found(auth_service, mock_db, mocker, app):
    request_data = {
        "username": "nonexistentuser",
        "password": "password123"
    }

    mocker.patch('app.repositories.user_repository.UserRepository.get_user_by_username', return_value=None)

    with app.test_request_context(json=request_data):
        mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))

        result_data, result_status = auth_service.login(mock_response)

        assert result_status == 401
        assert result_data.get_json() == {"error": "Invalid credentials"}

def test_login_internal_error(auth_service, mock_db, mocker, app):
    request_data = {
        "username": "testuser",
        "password": "password123"
    }

    mocker.patch('app.repositories.user_repository.UserRepository.get_user_by_username', side_effect=Exception("Database error"))

    with app.test_request_context(json=request_data):
        mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))

        result_data, result_status = auth_service.login(mock_response)

        assert result_status == 500
        assert result_data.get_json() == {"error": "Database error"}



