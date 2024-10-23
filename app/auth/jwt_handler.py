import jwt
from datetime import datetime, timedelta

class JWTHandler:
    """
    Class to handle creation and validation of JWT tokens.
    """

    def __init__(self, secret_key: str, algorithm: str = "HS256", expire_minutes: int = 30):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expire_minutes = expire_minutes

    def create_access_token(self, data: dict) -> str:
        """
        Creates a JWT access token with user data.
        :param data: Data that will be included in the token.
        :return: Token JWT with string.
        """
        to_encode = data.copy()
        expire = datetime.now() + timedelta(minutes=self.expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def verify_access_token(self, token: str) -> dict:
        """
        Checks the validity of a JWT access token.
        :param token: Token jwt to be checked.
        :return: Decoded data from token if valid.
        :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")
