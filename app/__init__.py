import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS 
from config import Config

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

# In-memory blacklist for tokens
blacklist = set()

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    return jwt_payload['jti'] in blacklist

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Enable CORS
    allowed_origins = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")  # Read from .env
    CORS(app, resources={r"/*": {"origins": allowed_origins}})  # Enable CORS for specified origins

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.controller import auth, health
    app.register_blueprint(auth.bp)
    app.register_blueprint(health.bp)

    return app
