import jwt
from app.config.settings import aplication_settings as  settings
from datetime import datetime, timedelta

def generate_test_jwt(user_id=1, username="testuser"):
    """
    Gera um token JWT de teste usando a chave secreta da aplicação.
    """
    payload = {
        "user_id": user_id,
        "username": username,
        "exp": datetime.now() + timedelta(minutes=60)
    }
    token = jwt.encode(payload, settings.secret_key, algorithm="HS256")
    return f"Bearer {token}"
