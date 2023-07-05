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


class Campers(Resource):
    def get(self):
        campers = [camper.to_dict() for camper in Camper.query.all()]

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
        return make_response(camper.to_dict(), 203)

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


class LunchBoxById(Resource):
    def get(self, id):
        lunch_box = Lunchbox.query.filter_by(id=id).first()
        if not lunch_box:
            abort(404, "Lunchbox not found")
        return make_response(
            lunch_box.to_dict(
                only=("id", "drink", "image", "snack", "camper.camper_name")
            ),
            200,
        )


api.add_resource(LunchBoxById, "/lunch_boxes/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
