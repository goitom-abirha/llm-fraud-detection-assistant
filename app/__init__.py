from flask import Flask
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-key"
    app.register_blueprint(bp)
    return app

