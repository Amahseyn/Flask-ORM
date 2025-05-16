# app/comments/models.py
from datetime import datetime
from app import db


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __init__(self, content, post_id, user_id):
        self.content = content
        self.post_id = post_id
        self.user_id = user_id
        

    def __repr__(self):
        return f'<Comment id={self.id} content={self.content} date_posted={self.date_posted}>'
