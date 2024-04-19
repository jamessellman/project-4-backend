from marshmallow import fields
from app import marsh
from models.comment_model import CommentModel


class CommentSerializer(marsh.SQLAlchemyAutoSchema):

    user_comments = fields.Nested("UserSerializer", many=False)

    class Meta:
        model = CommentModel
        load_instance = True
        include_fk = True
