from app import db
from models.base_model import BaseModel

from models.comment_model import CommentModel
from models.user_model import UserModel


class FootballerModel(db.Model, BaseModel):

    __tablename__ = "players"
    # defining comments in players table
    # ! This is going to be the unique ID for this model.
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    name = db.Column(db.Text, nullable=False)
    position = db.Column(db.Text, nullable=False)
    shirt_number = db.Column(db.Integer, nullable=False)
    nationality = db.Column(db.Text, nullable=False)
    club = db.Column(db.Text, nullable=True)
    career_goals = db.Column(db.Integer, nullable=False)
    career_appearances = db.Column(db.Integer, nullable=False)
    foot = db.Column(db.Text, nullable=False)
    bio = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

    # relationships between tables.
    # adding the column in player table for user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # adding the user model to player table
    user = db.relationship("UserModel", backref="users")

    # comment relationship
    comments = db.relationship(
        "CommentModel", backref="comments", cascade="all, delete"
    )
