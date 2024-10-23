from flask import Flask
from flasgger import Swagger
from app.db.database import engine, Base
from app.routes import api_auth

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(api_auth, url_prefix='/api/auth')

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
