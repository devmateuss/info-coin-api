from flask import Blueprint, make_response
from flasgger import swag_from
from app.schemas.auth_schema import auth_scheme
from app.services.authentication_service import AuthenticationService
from app.db.database import get_session
from app.config.settings import aplication_settings as settings

api_auth = Blueprint('auth', __name__, template_folder='routes')

@api_auth.route('/login', methods=['POST'])
@swag_from(auth_scheme)
def login():
    """
    Logs in a user and returns a JWT token.
    """
    with get_session() as db:
        try:
            auth_service = AuthenticationService(secret_key=settings.secret_key, db=db)
            return auth_service.login(response=make_response)
        except Exception as e:
            return make_response({"error": str(e)}, 500)
        finally:
            db.close()
