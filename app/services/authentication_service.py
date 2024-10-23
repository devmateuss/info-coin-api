# src/services/authentication_service.py

from sqlalchemy.orm import Session
from flask import jsonify, request, Response
from pydantic import ValidationError
from app.core.interfaces.base_auth_service import BaseAuthService
from app.auth.jwt_handler import JWTHandler
from app.repositories.user_repository import UserRepository
from app.db.database import SessionLocal
from app.config.settings import aplication_settings as settings
from app.models.auth_models import LoginRequest, LoginResponse

class AuthenticationService(BaseAuthService):
    """
    Concrete implementation of authentication service using JWTHandler.
    """

    def __init__(self, secret_key: str):
        self.jwt_handler = JWTHandler(
            secret_key=secret_key,
            algorithm='HS256',
            expire_minutes=settings.jwt_expire_minutes
        )

    def login(self, response: callable) -> Response:
        """
        Validates user credentials and returns a JWT token.
        :param response: HTTP response function.
        :return: HTTP response with token or error message.
        """
        db: Session = SessionLocal()
        try:
            try:
                login_data = LoginRequest(**request.json)
            except ValidationError as e:
                return response(jsonify({"error": e.errors()}), 400)

            user_repository = UserRepository(db)
            user = user_repository.get_user_by_username(login_data.username)

            if user and user.password == login_data.password:
                access_token = self.jwt_handler.create_access_token({"sub": login_data.username})
                login_response = LoginResponse(access_token=access_token)
                return response(jsonify(login_response.dict()), 200)
            else:
                return response(jsonify({"error": "Invalid credentials"}), 401)

        except Exception as e:
            return response(jsonify({"error": str(e)}), 500)
        finally:
            db.close()
