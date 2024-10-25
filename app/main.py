from flask import Flask
from flasgger import Swagger
from app.db.database import config_alchemy
from app.routes.auth_routes import api_auth
from app.routes.coin_routes import api_coin
from app.routes.user_routes import api_user
from app.schemas.swagger_docs import swagger_config, swagger_template

def create_app():
    app = Flask(__name__)

    swagger = Swagger(app, config=swagger_config, template=swagger_template)

    app.register_blueprint(api_user, url_prefix='/api/users')
    app.register_blueprint(api_auth, url_prefix='/api/auth')
    app.register_blueprint(api_coin, url_prefix='/api/infocoin')

    config_alchemy()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000)
