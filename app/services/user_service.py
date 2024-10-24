import bcrypt
from sqlalchemy.orm import Session
from flask import jsonify
from app.repositories.user_repository import UserRepository
from app.models.user_model import User

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: dict, response) -> dict:
        """
        Handles the creation of a new user, hashing the password before saving.
        :param user_data: A dictionary with 'username' and 'password'.
        :param response: A callable to create the HTTP response.
        :return: JSON response with the created user's information or error message.
        """
        try:
            username = user_data.get('username')
            password = user_data.get('password')

            # Validações básicas
            if not username or not password:
                return response(jsonify({"error": "Username and password are required"}), 400)

            # Criação do repositório de usuário
            user_repository = UserRepository(self.db)

            # Verificar se o usuário já existe
            if user_repository.get_user_by_username(username):
                return response(jsonify({"error": "User already exists"}), 400)

            # Hash da senha
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Criar e salvar o novo usuário
            user = User(username=username, password=hashed_password)
            user_repository.add_user(user)

            return response(jsonify({"message": "User created successfully", "username": user.username}), 201)
        except Exception as e:
            return response(jsonify({"error": str(e)}), 500)
