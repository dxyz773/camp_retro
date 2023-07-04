from flask import make_response, request, session
from flask_restful import Resource
from models import (
    Camper,
    Lunchbox,
    Snack,
    Drink,
    TreasureChest,
    Prize,
    Game,
    Token,
    CampfireStories,
)
from config import app, db, api


@app.route("/")
def index():
    return f"<h1>Welcome to Camp Retro</h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
