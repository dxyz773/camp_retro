from flask_migrate import Migrate
from flask_restful import Api
from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from flask_jwt_extended import JWTManager
import os


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)


app = Flask(__name__)

# app.config["SECRET_KEY"] = "4d7ec118c47131d09976e81dee7eaf1fb67d45a8144731f9"
app.secret_key = (
    '\x19\xb1\x0c}h\x1d\xf4\xc3\xb8\xf6\xcc#\x80\xae"\x80\x81~\xc8D$\xa4\xb9\x9e'
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///camp_retro.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False


db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)
api = Api(app)
