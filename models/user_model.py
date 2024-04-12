from app import db
from models.base_model import BaseModel
from models.comment_model import CommentModel


class UserModel(db.Model, BaseModel):
    # update the table name.
    __tablename__ = "users"

    # id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)

    # footballer = db.relationship("FootballerModel", backref="player")

    # comment relationship
    comments = db.relationship(
        "CommentModel", backref="user_comments", cascade="all, delete"
    )
