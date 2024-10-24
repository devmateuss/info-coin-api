# src/services/authentication_service.py

import jwt
import bcrypt
from datetime import datetime, timedelta
from typing import Callable
from sqlalchemy.orm import Session
from flask import request, jsonify
from app.repositories.user_repository import UserRepository
from app.config.settings import aplication_settings as settings

class AuthenticationService:
    def __init__(self, secret_key: str, db: Session):
        self.secret_key = secret_key
        self.db = db

    def login(self, response: Callable) -> dict:
        """
        Handles the login process, including validating the request data,
        checking user credentials, and generating a JWT token.
        :param response: A callable for creating the HTTP response.
        :return: JSON response with the JWT token or an error message.
        """
        try:
            # Extract data from the request
            data = request.json
            username = data.get('username')
            password = data.get('password')

            # Validate the received data
            if not username or not password:
                return response(jsonify({"error": "Username and password are required"}), 400)

            # Fetch user from the database using the repository
            user_repository = UserRepository(self.db)
            user = user_repository.get_user_by_username(username)
            
            # Verify user credentials
            if user and self.verify_password(password, user.password):
                # If credentials are valid, create a JWT token
                token = self.create_token(user.id)
                return response(jsonify({"access_token": token}), 200)
            else:
                return response(jsonify({"error": "Invalid credentials"}), 401)
        except Exception as e:
            return response(jsonify({"error": str(e)}), 500)

    def create_token(self, user_id: int) -> str:
        """
        Generates a JWT token for a user.
        :param user_id: The ID of the user.
        :return: A JWT token as a string.
        """
        expire_time = datetime.utcnow() + timedelta(minutes=settings.jwt_expire_minutes)
        payload = {
            "user_id": user_id,
            "exp": expire_time
        }
        token = jwt.encode(payload, self.secret_key, algorithm="HS256")
        return token

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifies the user's password against the stored hashed password.
        :param plain_password: The password provided by the user.
        :param hashed_password: The hashed password stored in the database.
        :return: True if the password matches, False otherwise.
        """
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    def hash_password(self, password: str) -> str:
        """
        Hashes a plain password for storage.
        :param password: The plain text password.
        :return: A hashed password.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
