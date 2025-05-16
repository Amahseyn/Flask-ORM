from app import db
from app.users.models import User  # Import User here
from datetime import datetime
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    user = db.relationship('User', back_populates='posts')

    def __repr__(self):
        return f'<Post id={self.id} title={self.title}>'