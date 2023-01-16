from flask import current_app
from flask_login import UserMixin

db = current_app.extentions["db"]

class User(db.Model, UserMixin):
    """User data model."""

    __tablename__ = "accounts_user"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True)

    password = db.Column(db.String(255))

    active = db.Column(db.Boolean(name='active'))
    
    def __str__(self):
        """Representation."""
        return 'User <id={0.id}, email={0.email}>'.format(self)
    
    @classmethod
    def valid_user():
        pass