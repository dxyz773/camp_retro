from flask_migrate import Migrate
from flask_restful import Api
from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_session import Session

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)


app = Flask(__name__)

app.config["SECRET_KEY"] = "4d7ec118c47131d09976e81dee7eaf1fb67d45a8144731f9"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///camp_retro.db"
app.config["SESSION_TYPE"] = "sqlalchemy"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(metadata=metadata)
app.config["SESSION_SQLALCHEMY"] = db
bcrypt = Bcrypt(app)
CORS(app)
api = Api(app)

migrate = Migrate(app, db)
db.init_app(app)

sess = Session(app)
# sess.init_app(app)
