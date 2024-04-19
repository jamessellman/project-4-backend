from http import HTTPStatus
from functools import wraps
from flask import request, g
import jwt
from config.environment import SECRET
from models.user_model import UserModel
from app import db


def secure_route(route_func):

    @wraps(route_func)
    def wrapper(*args, **kwargs):

        # GRAB THE TOKEN
        raw_token = request.headers.get("Authorization")
        print("RAW_TOKEN", raw_token)
        # IF NO TOKEN GO AWAY
        if not raw_token:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        # REMOVE BEARER FROM TOKEN
        clean_token = raw_token.replace("Bearer ", "")
        print("TOKEN:", clean_token)

        try:
            # DECODE THE TOKEN
            payload = jwt.decode(clean_token, SECRET, "HS256")
            # GET THE USER FROM THE TOKEN
            user_id = payload["sub"]
            # USER THE USER FROM DB WITH THIS ID
            user = db.session.query(UserModel).get(user_id)
            # ATTACH THIS UDER TO THE REQUEST FOR COMPARISION LATER
            g.current_user = user
            print("USER", user)

            return route_func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED
        except Exception as e:
            print(e)
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

    return wrapper
