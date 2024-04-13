from sqlalchemy.ext.hybrid import hybrid_property
from app import db, bcrypt
from models.base_model import BaseModel
from models.comment_model import CommentModel


class UserModel(db.Model, BaseModel):
    # update the table name.
    __tablename__ = "users"

    # id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)

    #    this is a temporary field on my user model before the password is hashed.
    @hybrid_property
    def password(self):
        pass

    # here we will use that temporary field to hash the password before saving to the DB.
    @password.setter
    def password(self, password_plaintext):
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_pw.decode("utf-8")

    # ! Add a method to our user model
    # ! to validate a password
    def validate_password(self, login_password):
        # ! We need both the password_hash on the account, and the login password
        return bcrypt.check_password_hash(self.password_hash, login_password)

    # footballer = db.relationship("FootballerModel", backref="player")

    # comment relationship
    comments = db.relationship(
        "CommentModel", backref="user_comments", cascade="all, delete"
    )
