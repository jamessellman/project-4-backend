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


# the function that geta single player
@router.route("/players/<int:id>", methods=["GET"])
def get_single_player_by_id(id):
    player = FootballerModel.query.get(id)
    print(player)
    return Football_Serializer.jsonify(player)


@router.route("/players", methods=["POST"])
def add_a_player():
    player_dictionary = request.json
    print("dictionary", player_dictionary)
    try:
        player = Football_Serializer.load(player_dictionary)
        print("player", player)
        db.session.add(player)
        db.session.commit()
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    return Football_Serializer.jsonify(player)
