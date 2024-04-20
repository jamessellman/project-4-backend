# blueprint It allows you to organize routes, templates,
# and static files into modular components,
# making your Flask application more maintainable and scalable.
from flask import Blueprint, request, g, jsonify
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
import random

from app import db

from serializers.comment_serializer import CommentSerializer
from serializers.footballer_serializer import FootballSerializer

from models.footballer_model import FootballerModel
from models.comment_model import CommentModel

from middleware.secure_route import secure_route


# ! Instantiate our serializer

Football_Serializer = FootballSerializer()
Comment_Serializer = CommentSerializer()

# ! Creating a instance of our Blueprint class, with the controller name and __name__
router = Blueprint("players", __name__)


# creating the routes


# the function that gets the players
@router.route("/players", methods=["GET"])
def get_players():
    players = FootballerModel.query.all()
    return Football_Serializer.jsonify(players, many=True)


# the function that gets a single player
@router.route("/players/<int:player_id>", methods=["GET"])
def get_single_player_by_id(player_id):
    player = FootballerModel.query.get(player_id)
    return Football_Serializer.jsonify(player)


@router.route("/players", methods=["POST"])
@secure_route
def add_a_player():

    player_dictionary = request.json
    player_dictionary["user_id"] = g.current_user.id
    try:
        player_to_add = Football_Serializer.load(player_dictionary)
        player_to_add.save()

    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    return Football_Serializer.jsonify(player_to_add)


# function that deletes a player
@router.route("/players/<int:player_id>", methods=["DELETE"])
@secure_route
def delete_a_player(player_id):
    # first we have to find the player to delete linking by id from request from client
    player_to_delete = FootballerModel.query.get(player_id)
    if not player_to_delete:
        return {"message": "No player found"}, HTTPStatus.NOT_FOUND
    try:
        if g.current_user.id == 1 or player_to_delete.user_id == g.current_user.id:
            player_to_delete.remove()
            return "", HTTPStatus.NO_CONTENT
        else:
            return {
                "message": "You are not authorized to remove this player"
            }, HTTPStatus.UNAUTHORIZED
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}


# function that edits a player
@router.route("/players/<int:player_id>", methods=["PUT"])
@secure_route
def player_to_edit(player_id):
    player_dictionary = request.json

    existing_player = FootballerModel.query.get(player_id)
    print(player_id)
    if not existing_player:
        return {"message": "No player found"}, HTTPStatus.NOT_FOUND

    try:
        if g.current_user.id == 1 or existing_player.user_id == g.current_user.id:
            print("1")
            player = Football_Serializer.load(
                player_dictionary, instance=existing_player, partial=True
            )
            print("2")
            player.save()
            print("3")
            return Football_Serializer.jsonify(player), HTTPStatus.OK
        else:
            return {
                "message": "You are not authorized to edit this player"
            }, HTTPStatus.UNAUTHORIZED
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}


# function to choose a random player
@router.route("player/random", methods=["GET"])
def select_random_profile():
    get_all_profile_ids = db.session.query(
        FootballerModel.id
    ).all()  # Get all profile IDs
    random_id = random.choice(get_all_profile_ids)[0]  # Select a random ID
    profile = FootballerModel.query.get(random_id)  # Retrieve the corresponding profile
    return Football_Serializer.jsonify(profile)


# FUNCTIONS FOR COMMENTS
# POST A COMMENT
@router.route("/comments/<int:player_id>/comments", methods=["POST"])
@secure_route
def create_comment(player_id):
    print("INSIDE COMMENTS")
    comment_dictionary = request.json
    comment_dictionary["user_id"] = g.current_user.id
    existing_player = FootballerModel.query.get(player_id)

    if not existing_player:
        print("3")
        return {"message": "No player found"}, HTTPStatus.NOT_FOUND
    comment_to_add = Comment_Serializer.load(comment_dictionary)
    comment_to_add.footballer_id = player_id
    comment_to_add.user_id = g.current_user.id
    comment_to_add.save()

    return Comment_Serializer.jsonify(comment_to_add), HTTPStatus.CREATED


# Delete a comment
@router.route("/comments/<int:comment_id>", methods=["DELETE"])
@secure_route
def delete_a_comment(comment_id):

    comment = CommentModel.query.get(comment_id)

    if not comment:
        return {"message": "No comment found"}, HTTPStatus.NOT_FOUND

    comment.remove()

    return "", HTTPStatus.NO_CONTENT


# get all comments
@router.route("/comments", methods=["GET"])
def get_all_comments():
    comments = CommentModel.query.all()
    return Comment_Serializer.jsonify(comments, many=True)


# get all comments by footballerID
@router.route("/comments/<int:footballer_id>", methods=["GET"])
def get_comments_by_footballer_id(footballer_id):
    comments = CommentModel.query.filter_by(footballer_id=footballer_id).all()
    print(comments)
    comment_serializer = CommentSerializer()
    return jsonify(comment_serializer.dump(comments, many=True))


# get all comments by user_id
# @router.route("/comments/<int:>", methods=["GET"])
# @secure_route
# def get_comments_by_user_id(user_id):
#     current_user = g.current_user.id
