from http import HTTPStatus
from datetime import datetime, timedelta, timezone
import jwt
from flask import Blueprint, request
from marshmallow.exceptions import ValidationError


from models.user_model import UserModel
from serializers.user_serializer import UserSerializer
from config.environment import SECRET

user_serializer = UserSerializer()


router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def signup_a_user():
    print("in user controller 1")
    user_dictionary = request.json

    try:
        user = user_serializer.load(user_dictionary)
        print("in user controller 1")
        user.save()
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}

    return user_serializer.jsonify(user)


@router.route("/login", methods=["POST"])
def login_a_user():
    print("in log in")
    # ! user provides a email & password
    user_dictionary = request.json
    # ! Check if the user with this email exists..
    user = UserModel.query.filter_by(email=user_dictionary["email"]).first()
    if not user:
        return {
            "message": "Your email or password was incorrect."
        }, HTTPStatus.UNAUTHORIZED
    if not user.validate_password(user_dictionary["password"]):
        return {
            "message": "Your email or password was incorrect."
        }, HTTPStatus.UNAUTHORIZED

    payload = {
        # this will expire 1 day from now
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
        # this will show the time the token was issued at
        "iat": datetime.now(timezone.utc),
        # also stick the user id on the token as sub
        "sub": user.id,
    }
    # ! Return a token to the user, so that they can use that token when doing things like POST a tea.

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    return {"message": "login success", "token": token}, HTTPStatus.ACCEPTED
