from http import HTTPStatus
from datetime import datetime, timedelta, timezone
import jwt
from flask import Blueprint, request, g, jsonify
from marshmallow.exceptions import ValidationError


from models.user_model import UserModel
from serializers.user_serializer import UserSerializer
from config.environment import SECRET
from middleware.secure_route import secure_route

user_serializer = UserSerializer()


router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def signup_a_user():
    print("in user controller 1")
    user_dictionary = request.json

    # ! Check the passwords
    if user_dictionary["password"] != user_dictionary["passwordConfirmation"]:
        return {
            "errors": "Passwords do not match",
            "messsages": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    # ! Delete the password conf field that marshmallow doens't know about.
    del user_dictionary["passwordConfirmation"]

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
    print("login success")
    return {"message": "login success", "token": token}, HTTPStatus.ACCEPTED


@router.route("/signup", methods=["GET"])
@secure_route
def get_current_user():
    try:
        current_user = g.current_user
        if current_user:
            return user_serializer.jsonify(current_user), 200
        else:
            return jsonify(message="Current user not found"), 404
    except Exception as e:
        print(e)
        return jsonify(message="There was an error, please try again later."), 500
