import os
import jwt
from functools import wraps
from flask import request, jsonify
from app.config.settings import aplication_settings as settings

def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization", None)
        if token is None:
            return jsonify({"error": "Authorization header is missing"}), 401
        
        if token.startswith("Bearer "):
            token = token.split(" ")[1]

        try:
            decoded_token = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
            request.user = decoded_token
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        
        return f(*args, **kwargs)
    
    return decorated_function
