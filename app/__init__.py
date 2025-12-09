from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")  

    # Importar e registrar blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.cadastro_routes import cadastro_bp
    from app.routes.solicitacao_routes import solicitacao_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(cadastro_bp)
    app.register_blueprint(solicitacao_bp)

    return app
