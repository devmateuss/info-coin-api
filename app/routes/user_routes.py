from flask import Blueprint, request, jsonify, make_response
from flasgger import swag_from
from app.db.database import get_session
from app.services.user_service import UserService
from app.schemas.create_user_docs import create_user_docs
from werkzeug.exceptions import BadRequest


api_user = Blueprint('user', __name__)

@api_user.route('/create', methods=['POST'])
@swag_from(create_user_docs)
def create_user():
    """
    Endpoint to create a new user.
    Expects JSON with 'username' and 'password'.
    """
    with get_session() as db:
        try:
            user_data = request.json

            user_service = UserService(db=db)
            return user_service.create_user(user_data, response=make_response)
        except BadRequest as e:
            return make_response(jsonify({"error": "Invalid request data: " + str(e.description)}), 400)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
