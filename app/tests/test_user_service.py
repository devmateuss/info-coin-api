import pytest
from unittest.mock import MagicMock
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.db.database import get_session

@pytest.fixture
def user_service(mocker):
    mock_session = MagicMock()
    mocker.patch("app.db.database.get_session", return_value=mock_session)
    return UserService(db=mock_session)

@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "password123"
    }

@pytest.fixture
def mock_get_user_by_username(mocker):
    return mocker.patch.object(UserRepository, "get_user_by_username", return_value=[])

@pytest.fixture
def mock_add_user(mocker):
    return mocker.patch.object(UserRepository, "add_user", return_value=None)

def test_create_user_success(
    mock_get_user_by_username,
    mock_add_user,
    user_service,
    user_data,
    mocker,
    app
):
    mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))

    with app.app_context():
        result_data, result_status = user_service.create_user(user_data, mock_response)

    assert result_status == 201
    assert result_data.get_json() == {"message": "User created successfully", "username": user_data["username"]}
    mock_add_user.assert_called_once()

def test_create_user_already_exists(
    user_service,
    user_data,
    mocker,
    app
):
    mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))
    mock_get_user_by_username = mocker.patch.object(
        UserRepository, 
        "get_user_by_username", 
        return_value=MagicMock()
    )

    with app.app_context():
        result_data, result_status = user_service.create_user(user_data, mock_response)

    assert result_status == 400
    assert result_data.get_json() == {"error": "User already exists"}
    mock_get_user_by_username.assert_called_once_with(user_data["username"])


def test_create_user_missing_data(
    user_service,
    mocker,
    app
):
    mock_response = mocker.MagicMock(side_effect=lambda data, status: (data, status))
    mock_get_user_by_username = mocker.patch.object(UserRepository, "get_user_by_username", return_value=None)

    with app.app_context():
        result_data, result_status = user_service.create_user({}, mock_response)

    assert result_status == 400
    assert result_data.get_json() == {"error": "Username and password are required"}
    mock_get_user_by_username.assert_not_called()