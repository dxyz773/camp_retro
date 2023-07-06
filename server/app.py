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


@app.before_request
def check_session():
    print(f"Before request: {session}")


@app.after_request
def check_session_2(response):
    print(f"After request: {session}")
    return response


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

    # ---------------------------------------------------------------------------|
    #                               SIGNUP
    # ---------------------------------------------------------------------------|
    def post(self):
        data = request.get_json()

        try:
            camper = Camper(
                username=data.get("username"),
                camper_name=data.get("camper_name"),
                image=data.get("image"),
                bio=data.get("bio"),
            )

            db.session.add(camper)
            db.session.commit()

        except:
            return make_response({"errors": ["validation errors"]}, 400)

        session["user_id"] = camper.id
        response = make_response(
            camper.to_dict(),
            201,
        )
        return response


api.add_resource(Campers, "/campers")


# ---------------------------------------------------------------------------|
#                               LOGIN
# ---------------------------------------------------------------------------|
@app.route("/login", methods=["POST"])
def login():
    username = request.get_json().get("username")

    camper = Camper.query.filter_by(username=username).first()
    if not camper:
        abort(401, "Unauthorized")
    session["user_id"] = camper.id
    return make_response(camper.to_dict(), 200)


# ---------------------------------------------------------------------------|
#                               LOGOUT
# ---------------------------------------------------------------------------|


@app.route("/logout", methods=["GET"])
def logout():
    session["user_id"] = None
    return make_response("", 204)


# ---------------------------------------------------------------------------|
#                               CHECK SESSION
# ---------------------------------------------------------------------------|
@app.route("/authorized-session", methods=["GET"])
def authorize():
    camper = Camper.query.filter_by(id=session.get("user_id")).first()
    if not camper:
        abort(401, "Unauthorized")
    return make_response(camper.to_dict(), 200)


# ---------------------------------------------------------------------------|
#                               CAMPER BY ID
# ---------------------------------------------------------------------------|


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
            abort(422, "Errors updading Lunchbox")
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
            abort(404, "Treasure not found")

        treasure_dict = treasure.to_dict(
            only=("id", "image", "prizes", "camper_id", "camper.camper_name")
        )
        return make_response(treasure_dict, 200)


api.add_resource(TreasureChestById, "/treasure_chests/<int:id>")

# ---------------------------------------------------------------------------|
#                             PRIZES
# ---------------------------------------------------------------------------|


class Prizes(Resource):
    def get(self):
        prizes = [
            prize.to_dict(
                only=(
                    "id",
                    "name",
                    "image",
                    "token_price",
                    "treasure_chest_id",
                    "treasure_chest",
                )
            )
            for prize in Prize.query.all()
        ]
        return make_response(prizes, 200)


api.add_resource(Prizes, "/prizes")


class PrizeById(Resource):
    def get(self, id):
        prize = Prize.query.filter_by(id=id).first()
        if not prize:
            abort(404, "Prize not found")

        prize_dict = prize.to_dict(
            only=(
                "id",
                "name",
                "image",
                "token_price",
                "treasure_chest_id",
                "treasure_chest.image",
            )
        )
        return make_response(prize_dict, 200)

    def patch(self, id):
        prize = Prize.query.filter_by(id=id).first()
        data = request.get_json()
        if not prize:
            abort(404, "Prize not found")
        try:
            for attr in data:
                setattr(prize, attr, data.get(attr))

            db.session.add(prize)
            db.session.commit()
        except:
            abort(422, "Errors updading Prize")
        return make_response(
            prize.to_dict(
                only=(
                    "id",
                    "name",
                    "image",
                    "token_price",
                    "treasure_chest_id",
                    "treasure_chest.image",
                )
            ),
            200,
        )


api.add_resource(PrizeById, "/prizes/<int:id>")


# ---------------------------------------------------------------------------|
#                               GAMES
# ---------------------------------------------------------------------------|
class Games(Resource):
    def get(self):
        games = [
            game.to_dict(
                only=(
                    "id",
                    "name",
                    "description",
                    "rules",
                    "image1",
                    "image2",
                    "image3",
                    "image4",
                    "token_id",
                    "tokens",
                    "win_status",
                )
            )
            for game in Game.query.all()
        ]
        return make_response(games, 200)

    def post(self):
        data = request.get_json()

        try:
            new_game = Game(
                name=data.get("name"),
                description=data.get("description"),
                rules=data.get("rules"),
                win_status=data.get("win_status"),
                image1=data.get("image1"),
                camper_id=data.get("camper_id"),
                token_id=data.get("token_id"),
            )

            db.session.add(new_game)
            db.session.commit()

        except:
            return make_response({"errors": ["validation errors"]}, 400)

        response = make_response(
            new_game.to_dict(
                only=(
                    "id",
                    "name",
                    "description",
                    "rules",
                    "image1",
                    "image2",
                    "image3",
                    "image4",
                    "token_id",
                    "tokens",
                )
            ),
            201,
        )
        return response


api.add_resource(Games, "/games")


class GameById(Resource):
    def get(self, id):
        game = Game.query.filter_by(id=id).first()
        if not game:
            abort(404, "Game not found")

        game_dict = game.to_dict(
            only=(
                "id",
                "name",
                "description",
                "rules",
                "win_status",
                "image1",
                "image2",
                "image3",
                "image4",
                "token_id",
                "tokens",
                "camper.camper_name",
            )
        )
        return make_response(game_dict, 200)

    def patch(self, id):
        game = Game.query.filter_by(id=id).first()
        data = request.get_json()
        if not game:
            abort(404, "Game not found")
        try:
            for attr in data:
                setattr(game, attr, data.get(attr))

            db.session.add(game)
            db.session.commit()
        except:
            abort(422, "Errors updading Prize")
        return make_response(
            game.to_dict(
                only=(
                    "id",
                    "name",
                    "description",
                    "rules",
                    "win_status",
                    "image1",
                    "image2",
                    "image3",
                    "image4",
                    "token_id",
                    "tokens",
                )
            ),
            200,
        )


api.add_resource(GameById, "/games/<int:id>")


# ---------------------------------------------------------------------------|
#                               TOKENS
# ---------------------------------------------------------------------------|
class TokensById(Resource):
    def get(self, id):
        token = Token.query.filter_by(id=id).first()
        if not token:
            abort(404, "Token not found")

        token_dict = token.to_dict(only=("id", "image", "amount", "game.name"))
        return make_response(token_dict, 200)


api.add_resource(TokensById, "/tokens/<int:id>")

# ---------------------------------------------------------------------------|
#                            CAMPFIRE STORIES
# ---------------------------------------------------------------------------|


class CampfireStories(Resource):
    def get(self):
        stories = [story.to_dict() for story in CampfireStory.query.all()]
        return make_response(stories, 200)


api.add_resource(CampfireStories, "/campfire_stories")


class CampfireStoryById(Resource):
    def get(self, id):
        story = CampfireStory.query.filter_by(id=id).first()
        if not story:
            abort(404, "Campfire story not found")

        story_dict = story.to_dict()
        return make_response(story_dict, 200)


api.add_resource(CampfireStoryById, "/campfire_stories/<int:id>")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
