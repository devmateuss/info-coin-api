from sqlalchemy.orm import Session

from app.core.interfaces.base_user_repository import BaseUserRepository
from app.models.user_model import User


class UserRepository(BaseUserRepository):
    """
    Repository to interact with the users table.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(self, username: str) -> User:
        """
        Search for a user by username.
        """
        return self.db.query(User).filter(User.username == username).first()
