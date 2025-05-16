# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager  # Importing JWTManager
from app.config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
# login_manager = LoginManager()
jwt = JWTManager()  # Initialize JWT Manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)
    jwt.init_app(app)  # Initialize JWT with the app

    # Register Blueprints
    from app.users.routes import users_bp
    from app.posts.routes import posts_bp
    from app.comments.routes import comments_bp
    from app.orders.routes import orders_bp
    from app.users.models import User
    from app.posts.models import Post
    from app.comments.models import Comment

    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(posts_bp, url_prefix='/posts')
    app.register_blueprint(comments_bp, url_prefix='/comments')
    app.register_blueprint(orders_bp, url_prefix='/orders')

    return app
