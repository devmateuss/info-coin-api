from flask import Blueprint, request, jsonify, make_response
from flasgger import swag_from
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.user_service import UserService
from app.schemas.create_user_docs import create_user_docs

api_user = Blueprint('user', __name__)

@api_user.route('/create', methods=['POST'])
@swag_from(create_user_docs)
def create_user():
    """
    Endpoint to create a new user.
    Expects JSON with 'username' and 'password'.
    """
    db: Session = SessionLocal()
    try:
        user_data = request.json

        # Criação do serviço de usuário
        user_service = UserService(db=db)

        # Delegar a criação do usuário ao serviço de usuário
        return user_service.create_user(user_data, response=make_response)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)
    finally:
        db.close()
