from marshmallow import fields
from app import marsh
from models.footballer_model import FootballerModel


# creating a class for serialization
class FootballSerializer(marsh.SQLAlchemyAutoSchema):

    user = fields.Nested("UserSerializer", many=False)

    # add a nested class
    class Meta:
        # tell the serializer about the model and what to do with it.
        model = FootballerModel
        load_instance = True
        include_fk = True
