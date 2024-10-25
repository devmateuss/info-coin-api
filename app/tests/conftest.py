from unittest import mock
from unittest.mock import MagicMock, patch
import pytest
from app.db.database import Config
from app.main import create_app
from sqlalchemy.orm import Session
from app.services.authentication_service import AuthenticationService
from app.services.coin_service import CoinService
from app.services.user_service import UserService

@pytest.fixture(autouse=True)
def app(mocker):
    mocker.patch("app.db.database.create_engine", return_value=MagicMock())
    mocker.patch("app.db.database.create_all_tables", return_value=None)

    mocker.patch.object(Config, "session_maker", return_value=MagicMock())

    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture
def mock_jwt_decode():
    with patch('app.common.auth_decorator.jwt.decode') as mock_decode:
        mock_decode.return_value = {
            "user_id": 1,
            "username": "testuser",
            "exp": 1729795145 
        }
        yield mock_decode

@pytest.fixture
def auth_token():
    return 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InRlc3R1c2VyIiwiZXhwIjoxNzI5Nzk1MTQ1fQ.H-HXCQUMuuFjU7PG6gUfTtN7FvTGdZ-jnE-Dsohfwt4'

@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)

@pytest.fixture
def auth_service(mock_db):
    secret_key = "test_secret"
    return AuthenticationService(secret_key=secret_key, db=mock_db)

@pytest.fixture
def coin_service():
    return CoinService()


@pytest.fixture
def mock_db_session():
    return MagicMock(spec=Session)

@pytest.fixture
def user_service(mock_db_session):
    return UserService(db=mock_db_session)

@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "password123"
    }