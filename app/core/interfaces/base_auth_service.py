from abc import ABC, abstractmethod

class BaseAuthService(ABC):
    """
    Interface for the authentication service.
    Defines the methods that an authentication service class must implement.
    """

    @abstractmethod
    def login(self, username: str) -> str:
        """
        Generates an authentication token for a user.
        """
        raise NotImplementedError()
