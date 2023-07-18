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
from config import app, db, api
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
import ipdb

login_manager = LoginManager()
login_manager.init_app(app)


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
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


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

        new_lunch = Lunchbox(
            user_id=new_user.id,
            image="https://buyrocknroll.rocks/cdn/shop/products/c61284d5-d092-5772-893c-5753c244ea31_1000x.jpg?v=1552155505",
        )
        db.session.add(new_lunch)
        db.session.commit()

        new_treasure = TreasureChest(
            image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
            user_id=new_user.id,
        )
        db.session.add(new_treasure)
        db.session.commit()

        login_user(new_user, remember=True)

        response = make_response(
            new_user.to_dict(),
            201,
        )
        return response


api.add_resource(Signup, "/signup")


# ---------------------------------------------------------------------------|
#                               LOGIN
# ---------------------------------------------------------------------------|


class Login(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data.get("username", None)
            password = data.get("password", None)
            user = User.query.filter_by(username=username).first()
            if user:
                if user.authenticate(password):
                    login_user(user, remember=True)
                    return user.to_dict(), 200
            if not user:
                return {"error": "404 user not found"}, 404
        except:
            return {"error": "401 Unauthorized"}, 401


api.add_resource(Login, "/login")

# ---------------------------------------------------------------------------|
#                               LOGOUT
# ---------------------------------------------------------------------------|


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return make_response({}, 200)


# ---------------------------------------------------------------------------|
#                               CHECK SESSION
# ---------------------------------------------------------------------------|


class CheckSession(Resource):
    def get(self):
        user = User.query.filter_by(id=8).first()
        login_user(user, remember=True)
        return make_response(
            user.to_dict(rules=("-_password_hash",)),
            200,
        )
        # if current_user.is_authenticated:
        #     user = current_user.to_dict()
        #     ipdb.set_trace()
        #     return make_response(user, 200)
        # return make_response("Error, Unauthorized", 401)


api.add_resource(CheckSession, "/check_session")


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
            abort(422, "Errors updating Lunchbox")
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

    # def patch(self, id):
    #     treasure = TreasureChest.query.filter_by(id=id).first()
    #     data = request.get_json()
    #     if not treasure:
    #         abort(404, "Treasure not found")
    #     try:
    #         for attr in data:
    #             setattr(treasure, attr, data.get(attr))

    #         db.session.add(treasure)
    #         db.session.commit()
    #     except:
    #         abort(422, "Errors updating Treasure Chest")
    #     return make_response(
    #         treasure.to_dict(),
    #         200,
    #     )


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
                    "treasure_chest.image",
                )
            )
            for prize in Prize.query.all()
        ]
        return make_response(prizes, 200)

    def post(self):
        data = request.get_json()

        try:
            new_prize = Prize(
                name=data.get("name"),
                image=data.get("image"),
                token_price=data.get("token_price"),
                treasure_chest_id=data.get("treasure_chest_id"),
            )

            db.session.add(new_prize)
            db.session.commit()

        except:
            return make_response({"errors": ["validation errors"]}, 400)

        response = make_response(
            new_prize.to_dict(),
            201,
        )
        return response


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
