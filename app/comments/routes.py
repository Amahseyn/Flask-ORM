# app/comments/routes.py
from flask import Blueprint, request, jsonify
from app.comments.models import db, Comment
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

comments_bp = Blueprint('comments', __name__)

# Create Comment
@comments_bp.route('/create', methods=['POST'])
@jwt_required()
def create_comment():
    data = request.get_json()
    user_id = get_jwt_identity()

    comment = Comment(
        content=data['content'],
        post_id=data['post_id'],
        user_id=user_id,
        date_posted=datetime.utcnow()
    )

    db.session.add(comment)
    db.session.commit()

    return jsonify({"message": "Comment created successfully"}), 201

# Read All Comments for a Post
@comments_bp.route('/post/<int:post_id>', methods=['GET'])
@jwt_required()
def get_comments_for_post(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify([
        {
            "id": c.id,
            "content": c.content,
            "user_id": c.user_id,
            "post_id": c.post_id,
            "date_posted": c.date_posted.isoformat()
        } for c in comments
    ]), 200

# Update Comment
@comments_bp.route('/<int:comment_id>', methods=['PUT'])
@jwt_required()
def update_comment(comment_id):
    data = request.get_json()
    user_id = get_jwt_identity()

    comment = Comment.query.get_or_404(comment_id)

    if comment.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    comment.content = data['content']
    db.session.commit()

    return jsonify({"message": "Comment updated successfully"}), 200

# Delete Comment
@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comment_id):
    user_id = get_jwt_identity()
    comment = Comment.query.get_or_404(comment_id)

    if comment.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "Comment deleted successfully"}), 200
