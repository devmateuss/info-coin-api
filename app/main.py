from flask import Flask
from flasgger import Swagger
from app.db.database import engine, Base
from app.routes import api_auth, api_coin, api_user
from app.schemas.swagger_docs import swagger_config, swagger_template

app = Flask(__name__)
swagger = Swagger(app, config=swagger_config, template=swagger_template)

app.register_blueprint(api_user, url_prefix='/api/users')
app.register_blueprint(api_auth, url_prefix='/api/auth')
app.register_blueprint(api_coin, url_prefix='/api/infocoin')

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
