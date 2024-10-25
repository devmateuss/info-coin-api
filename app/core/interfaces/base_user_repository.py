from abc import ABC, abstractmethod
from app.models.user_model import User

class BaseUserRepository(ABC):
    """
    Interface for the user repository.
    """

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        """
        Search for a user by username.
        """
        raise NotImplementedError()
    
    @abstractmethod
    def add_user(self, user: User) -> User:
        """
        Create a new user in the database.
        """
        raise NotImplementedError
    

