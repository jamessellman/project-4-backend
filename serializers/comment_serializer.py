from app import marsh
from models.comment_model import CommentModel


class CommentSerializer(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentModel
        load_instance = True
        include_fk = True
