# app/users/routes.py
from flask import Blueprint, request, jsonify
from app.users.models import db, User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from functools import wraps

bcrypt = Bcrypt()
users_bp = Blueprint('users', __name__)

# Helper decorator to check for admin role in JWT token
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if user is None or user.role != 'admin':
            return jsonify({"message": "Admin privilege required"}), 403
        return fn(*args, **kwargs)
    return wrapper

# Register a user (only admin can create admin users)
@users_bp.route('/register', methods=['POST'])
@jwt_required()  # Require any authenticated user to register
def register():
    data = request.get_json()

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already exists"}), 400
    
    role = data.get('role', 'user')  # default role is user

    # Only admin can create admin users
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if role == 'admin' and (current_user is None or current_user.role != 'admin'):
        return jsonify({"message": "Only admins can create admin users"}), 403

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    user = User(username=data['username'], email=data['email'], password=hashed_password, role=role)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()
    if user and bcrypt.check_password_hash(user.password, data.get('password')):
        access_token = create_access_token(identity=str(user.id))  # <-- identity as string
        return jsonify({"access_token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Logout User (JWT doesn't have server-side logout by default, so just a placeholder)
@users_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # With JWT, logout is usually handled client-side by deleting the token.
    # You can implement token revocation if needed.
    return jsonify({"message": "Logout successful (delete your token client-side)"}), 200
