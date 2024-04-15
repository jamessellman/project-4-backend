# blueprint It allows you to organize routes, templates,
# and static files into modular components,
# making your Flask application more maintainable and scalable.
from flask import Blueprint, request, g
from http import HTTPStatus
from marshmallow.exceptions import ValidationError

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


# funtion that adds a player
@router.route("/players", methods=["POST"])
@secure_route
def add_a_player():
    player_dictionary = request.json
    player_dictionary["user_id"] = g.current_user.id
    player_dictionary["admin_id"] = 1
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
            player = Football_Serializer.load(
                player_dictionary, instance=existing_player, partial=True
            )
            player.save()
            return Football_Serializer.jsonify(player), HTTPStatus.OK
        else:
            return {
                "message": "You are not authorized to edit this player"
            }, HTTPStatus.UNAUTHORIZED
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}


# FUNCTIONS FOR COMMENTS
# POST A COMMENT
@router.route("/comments/<int:player_id>/comments", methods=["POST"])
@secure_route
def create_comment(player_id):
    print("INSIDE COMMENTS")
    comment_dictionary = request.json
    existing_player = FootballerModel.query.get(player_id)
    if not existing_player:
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
