from flask import Blueprint, make_response
from flasgger import swag_from
from app.services.authentication_service import AuthenticationService
from app.config.settings import aplication_settings as settings
from app.schemas import auth_scheme

api_auth = Blueprint('auth', __name__, template_folder='routes')

auth_service = AuthenticationService(secret_key=settings.secret_key)

@api_auth.route('/login', methods=['POST'])
@swag_from(auth_scheme)
def login():
    return auth_service.login(response=make_response)
