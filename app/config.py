import os

class Config:
    """Base configuration class."""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sec10ret_key'  # Used for session and CSRF protection. Set a unique value in production.
    FLASK_APP = os.environ.get('FLASK_APP') or 'run.py'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'  # 'development', 'production', etc.
    DEBUG = True if FLASK_ENV == 'development' else False  # Only enable debug mode in development.
    
    # Database settings (PostgreSQL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To disable Flask-SQLAlchemy's modification tracking, which reduces overhead.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:m102030m@localhost/flask'
    # Make sure you set the DATABASE_URL environment variable or adjust the connection string accordingly.

    # Flask-Login settings
    LOGIN_VIEW = 'users.login'  # Define the view that the user will be redirected to if not authenticated.
    LOGIN_MESSAGE = "Please log in to access this page."

    # Security settings (flask-bcrypt)
    BCRYPT_LOG_ROUNDS = 12  # Adjust based on your performance/security needs. A higher number is more secure but slower.

    # Flask-Migrate settings
    SQLALCHEMY_ECHO = False  # Set to True for verbose SQL logging (helpful in debugging, but can be verbose in production).

    # Additional configuration settings (these can be adjusted based on your needs):
    
    # For email configuration, if you plan to send emails (for password resets, confirmations, etc.)
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 587  # or 465 if using SSL
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'noreply@example.com'
    
    # Session timeout (if you need to set session expiration times)
    PERMANENT_SESSION_LIFETIME = os.environ.get('SESSION_TIMEOUT') or 3600  # 1 hour session timeout by default
    
    # JWT configuration (if using JWT for authentication)
    JWT_SECRET_KEY =   'secret10secert'  # Keep this secret in production
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or 3600*24*30*12  # Default 1 hour for access token expiration
