from flask import Blueprint, request, jsonify
from app.posts.models import Post, db
from flask_jwt_extended import jwt_required, get_jwt_identity

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/create', methods=['POST'])
@jwt_required()
def create_post():
    user_id = int(get_jwt_identity())  # convert identity string back to int
    data = request.get_json()
    post = Post(title=data['title'], content=data['content'], user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return jsonify({"message": "Post created successfully"}), 201

# Get All Posts
@posts_bp.route('/all', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([
        {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "user_id": post.user_id,
            "date_posted": post.date_posted.isoformat()
        } for post in posts
    ])

# Get Post by ID
@posts_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return jsonify({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "user_id": post.user_id,
            "date_posted": post.date_posted.isoformat()
        })
    return jsonify({"message": "Post not found"}), 404
