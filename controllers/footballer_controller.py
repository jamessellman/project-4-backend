# blueprint It allows you to organize routes, templates,
# and static files into modular components,
# making your Flask application more maintainable and scalable.
from flask import Blueprint, request
from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from app import db
from serializers.footballer_serializer import FootballSerializer
from models.footballer_model import FootballerModel

# ! Instantiate our serializer

Football_Serializer = FootballSerializer()


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
def add_a_player():
    player_dictionary = request.json
    try:
        player_to_add = Football_Serializer.load(player_dictionary)
        db.session.add(player_to_add)
        db.session.commit()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    return Football_Serializer.jsonify(player_to_add)


# function that deletes a player
@router.route("/players/<int:player_id>", methods=["DELETE"])
def delete_a_player(player_id):
    # first we have to find the player to delete linking by id from request from client
    player_to_delete = FootballerModel.query.get(player_id)

    if not player_to_delete:
        return {"message": "No player found"}, HTTPStatus.NOT_FOUND

    player_to_delete.remove()

    return "", HTTPStatus.NO_CONTENT


# function that edits a player
@router.route("/players/<int:player_id>", methods=["PUT"])
def player_to_edit(player_id):
    player_dictionary = request.json

    existing_player = FootballerModel.query.get(player_id)
    print(player_id)
    if not existing_player:
        return {"message": "No player found"}, HTTPStatus.NOT_FOUND

    try:
        player = Football_Serializer.load(
            player_dictionary, instance=existing_player, partial=True
        )

        player.save()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
    return Football_Serializer.jsonify(player), HTTPStatus.OK
