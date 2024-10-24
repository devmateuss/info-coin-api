from app.repositories.user_repository import UserRepository
from app.models.user_model import User

def test_create_user(db_session):
    user_data = {"name": "Test User", "email": "test@example.com"}
    repo = UserRepository(db_session)

    user = repo.create_user(user_data)  

    assert user.id is not None
    assert user.name == "Test User"
    assert user.email == "test@example.com"

def test_get_user_by_id(db_session):
    user_data = {"name": "Another User", "email": "another@example.com"}
    repo = UserRepository(db_session)

    user = repo.create_user(user_data)
    fetched_user = repo.get_user_by_username(user.email)

    assert fetched_user is not None
    assert fetched_user.name == "Another User"
    assert fetched_user.email == "another@example.com"
