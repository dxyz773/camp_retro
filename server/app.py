from flask import make_response, request, session, abort
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
    CampfireStory,
)
from config import app, db, api


@app.route("/")
def index():
    return f"<h1>Welcome to Camp Retro</h1>"


# ---------------------------------------------------------------------------|
#                               CAMPERS
# ---------------------------------------------------------------------------|


class Campers(Resource):
    def get(self):
        campers = [
            camper.to_dict(only=("id", "camper_name", "username", "image"))
            for camper in Camper.query.all()
        ]

        return make_response(campers, 200)

    def post(self):
        data = request.get_json()
        new_camper = Camper(
            username=data.get("username"),
            _password_hash=data.get("_password_hash"),
            camper_name=data.get("camper_name"),
            image=data.get("image"),
            bio=data.get("bio"),
        )
        try:
            db.session.add(new_camper)
            db.session.commit()
        except:
            abort(422, "Errors creating Camper")
        return make_response(new_camper.to_dict(), 201)


api.add_resource(Campers, "/campers")


class CamperById(Resource):
    def get(self, id):
        camper = Camper.query.filter_by(id=id).first()
        if not camper:
            abort(404, "Camper not found")

        camper_dict = camper.to_dict()
        return make_response(camper_dict, 200)

    def patch(self, id):
        camper = Camper.query.filter_by(id=id).first()
        data = request.get_json()
        if not camper:
            abort(404, "Camper not found")
        try:
            for attr in data:
                setattr(camper, attr, data.get(attr))
            db.session.add(camper)
            db.session.commit()
        except:
            abort(422, "Errors updading Camper")
        return make_response(camper.to_dict(), 200)

    def delete(self, id):
        camper = Camper.query.filter_by(id=id).first()
        if not camper:
            abort(404, "Camper not found")
        try:
            db.session.delete(camper)
            db.session.commit()
        except:
            abort(422, "Error deleting Camper")
        return make_response({}, 200)


api.add_resource(CamperById, "/campers/<int:id>")
# ---------------------------------------------------------------------------|
#                             LUNCH BOXES
# ---------------------------------------------------------------------------|


class LunchBoxById(Resource):
    def get(self, id):
        lunch_box = Lunchbox.query.filter_by(id=id).first()
        if not lunch_box:
            abort(404, "Lunchbox not found")
        return make_response(
            lunch_box.to_dict(
                only=(
                    "id",
                    "drink",
                    "image",
                    "snack",
                    "camper.camper_name",
                    "snack_id",
                    "drink_id",
                )
            ),
            200,
        )

    def patch(self, id):
        lunch_box = Lunchbox.query.filter_by(id=id).first()
        data = request.get_json()
        if not lunch_box:
            abort(404, "Lunchbox not found")
        try:
            for attr in data:
                setattr(lunch_box, attr, data.get(attr))

            db.session.add(lunch_box)
            db.session.commit()
        except:
            abort(422, "Errors updading Camper")
        return make_response(
            lunch_box.to_dict(
                only=(
                    "id",
                    "drink",
                    "image",
                    "snack",
                    "camper.camper_name",
                    "snack_id",
                    "drink_id",
                )
            ),
            200,
        )


api.add_resource(LunchBoxById, "/lunch_boxes/<int:id>")
# ---------------------------------------------------------------------------|
#                                  SNACKS
# ---------------------------------------------------------------------------|


class Snacks(Resource):
    def get(self):
        snacks = [
            snack.to_dict(only=("id", "name", "image")) for snack in Snack.query.all()
        ]
        return make_response(snacks, 200)


api.add_resource(Snacks, "/snacks")


class SnackById(Resource):
    def get(self, id):
        snack = Snack.query.filter_by(id=id).first()
        if not snack:
            abort(404, "Snack not found")
        snack_dict = snack.to_dict(only=("id", "name", "image"))
        return make_response(snack_dict, 200)


api.add_resource(SnackById, "/snacks/<int:id>")

# ---------------------------------------------------------------------------|
#                                 DRINKS
# ---------------------------------------------------------------------------|


class Drinks(Resource):
    def get(self):
        drinks = [
            drink.to_dict(only=("id", "name", "image")) for drink in Drink.query.all()
        ]
        return make_response(drinks, 200)


api.add_resource(Drinks, "/drinks")


class DrinkById(Resource):
    def get(self, id):
        drink = Drink.query.filter_by(id=id).first()
        if not drink:
            abort(404, "Drink not found")
        drink_dict = drink.to_dict(only=("id", "name", "image"))
        return make_response(drink_dict, 200)


api.add_resource(DrinkById, "/drinks/<int:id>")


# ---------------------------------------------------------------------------|
#                             TREASURE CHESTS
# ---------------------------------------------------------------------------|
class TreasureChestById(Resource):
    def get(self, id):
        treasure = TreasureChest.query.filter_by(id=id).first()
        if not treasure:
            abort(404, "Camper not found")

        treasure_dict = treasure.to_dict(
            only=("id", "image", "prizes", "camper_id", "camper.camper_name")
        )
        return make_response(treasure_dict, 200)


api.add_resource(TreasureChestById, "/treasure_chests/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
