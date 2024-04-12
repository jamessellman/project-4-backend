from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from config.environment import db_URI


app = Flask(__name__)

# used to set the uri to sqlachemy database. (it specifys to location of the db)
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

db = SQLAlchemy(app)
# instantiate marshmellow to tell it about flask
marsh = Marshmallow(app)


# @app.route("/hello", methods={"GET"})
# def hello_world():
#     return "<p>Hello, World!</p>"


from controllers import footballer_controller

app.register_blueprint(footballer_controller.router, url_prefix="/api")
