from app import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')

    posts = db.relationship('Post', back_populates='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def is_admin(self):
        return self.role == 'admin'
