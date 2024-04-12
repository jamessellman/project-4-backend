from app import db
from models.base_model import BaseModel


class CommentModel(db.Model, BaseModel):

    __tablename__ = "comments"

    content = db.Column(db.Text, nullable=False)

    # extra columns in the table, to that links to other tables. using footballer id and user id
    footballer_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
