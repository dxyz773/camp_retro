from flask import make_response, request, session, abort, jsonify
from flask_restful import Resource
from models import (
    User,
    Lunchbox,
    Snack,
    Drink,
    TreasureChest,
    Prize,
    Game,
    Token,
    CampfireStory,
)
from config import app, db, api, jwt

from flask_cors import cross_origin
import datetime
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    current_user,
)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


# ---------------------------------------------------------------------------|
#                      BEFORE AND AFTER REQUEST
# ---------------------------------------------------------------------------|
@app.before_request
def check_session():
    print(f"Before request: {session}")


@app.after_request
def check_session_2(response):
    print(f"After request: {session}")
    return response


# ---------------------------------------------------------------------------|
#                       FOR FLASK LOGIN
# ---------------------------------------------------------------------------|


# ---------------------------------------------------------------------------|
#                               SIGNUP
# ---------------------------------------------------------------------------|
class Signup(Resource):
    def post(self):
        data = request.get_json()
        new_user = User(username=data.get("username"))
        new_user.password_hash = data.get("password")

        db.session.add(new_user)
        db.session.commit()
        access_token = create_access_token(identity=new_user)
        response = make_response(
            jsonify(access_token=access_token),
            201,
        )
        return response


api.add_resource(Signup, "/signup")


# ---------------------------------------------------------------------------|
#                               LOGIN
# ---------------------------------------------------------------------------|
@app.route("/login", methods=["POST"])
@cross_origin(
    methods=["POST"],
    supports_credentials=True,
    headers=["Content-Type", "Authorization"],
)
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).one_or_none()
    if not user:
        return make_response("User not found", 404)
    if user.authenticate(password):
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)
    else:
        return make_response("Unauthorized. Credentials cannot be authenticated", 401)


# ---------------------------------------------------------------------------|
#                               LOGOUT
# ---------------------------------------------------------------------------|


class Logout(Resource):
    def get(self):
        return make_response({}, 200)


api.add_resource(Logout, "/logout")

# ---------------------------------------------------------------------------|
#                               CHECK SESSION
# ---------------------------------------------------------------------------|


@app.route("/check_session", methods=["GET"])
@jwt_required()
def check_session():
    if current_user:
        return jsonify(
            id=current_user.id,
            username=current_user.username,
            camper_name=current_user.camper_name,
            image=current_user.image,
            bio=current_user.bio,
        )


# ---------------------------------------------------------------------------|
#                               USERS
# ---------------------------------------------------------------------------|


class Users(Resource):
    def get(self):
        users = [
            user.to_dict(only=("id", "camper_name", "username", "image", "bio"))
            for user in User.query.all()
        ]

        return make_response(users, 200)


api.add_resource(Users, "/users")


class UserById(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")

        user_dict = user.to_dict()
        return make_response(user_dict, 200)

    def patch(self, id):
        data = request.get_json()
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        try:
            for attr in data:
                setattr(user, attr, data.get(attr))
            db.session.add(user)
            db.session.commit()
        except:
            abort(422, "Errors updating User")
        return make_response(user.to_dict(), 200)

    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        try:
            db.session.delete(user)
            db.session.commit()
        except:
            abort(422, "Error deleting User")
        return make_response({}, 200)


api.add_resource(UserById, "/users/<int:id>")


# ---------------------------------------------------------------------------|
#                             LUNCH BOXES
# ---------------------------------------------------------------------------|
class Lunchboxes(Resource):
    def post(self):
        data = request.get_json()

        try:
            new_lunch = Lunchbox(
                user_id=data.get("user_id"),
                image="image",
            )
            db.session.add(new_lunch)
            db.session.commit()

        except:
            return make_response({"errors": ["validation errors"]}, 400)

        response = make_response(new_lunch.to_dict(), 201)
        return response


api.add_resource(Lunchboxes, "/lunch_boxes")


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
                    "user.camper_name",
                    "snack_id",
                    "drink_id",
                    "user_id",
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
                    "user.camper_name",
                    "snack_id",
                    "drink_id",
                    "user_id",
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
            only=("id", "image", "prizes", "user_id", "user.camper_name")
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
                user_id=data.get("user_id"),
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
                "user.camper_name",
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
