from marshmallow import fields, ValidationError
from app import marsh
from models.user_model import UserModel


# password validation
def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Ensure you password is at least 8 characters long!")
    special_characters = "!@#$%^&*()-_=+{}[]"
    if not any(char in special_characters for char in password):
        raise ValidationError("Ensure you password contains a special character")


class UserSerializer(marsh.SQLAlchemyAutoSchema):

    # ! Add custom validation to our password!
    password = fields.String(required=True, validate=validate_password)

    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("email", "password_hash", "password")
