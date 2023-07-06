from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db
from config import bcrypt
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property


class Camper(db.Model, SerializerMixin):
    __tablename__ = "campers"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    camper_name = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    bio = db.Column(db.Text)
    # Relationships
    lunch_box = db.relationship(
        "Lunchbox", back_populates="camper", cascade="all, delete-orphan"
    )
    treasure_chest = db.relationship(
        "TreasureChest", back_populates="camper", cascade="all, delete-orphan"
    )
    games = db.relationship(
        "Game", back_populates="camper", cascade="all, delete-orphan"
    )
    # Association Proxy
    snack = association_proxy("lunch_box", "snack")
    drink = association_proxy("lunch_box", "drink")
    prizes = association_proxy("treasure_chest", "prizes")
    tokens = association_proxy("games", "tokens")
    # Serialize Rules
    serialize_rules = (
        "-created",
        "-updated",
        "-lunch_box.camper",
        "-treasure_chest.camper",
        "-games.camper",
    )

    # Bcrypt
    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)

    # Validations
    @validates("username")
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username is required")
        elif not len(username) > 1:
            raise ValueError("Username must be greater than 1 character")
        elif Camper.query.filter(Camper.username == username).first():
            raise ValueError("Username must be unique")
        else:
            return username

    @validates("camper_name")
    def validate_camper_name(self, key, camper_name):
        if not camper_name:
            raise ValueError("Camper name is required")
        return camper_name

    @validates("_password_hash")
    def validate_password_is_there(self, key, _password_hash):
        if not _password_hash:
            raise ValueError("Password is required")
        return _password_hash

    # __repr__
    def __repr__(self):
        return f"<Camper {self.username}, camper_name: {self.camper_name}>"


class Lunchbox(db.Model, SerializerMixin):
    __tablename__ = "lunch_boxes"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    image = db.Column(db.String, nullable=False)
    # Foreign Key(s)
    camper_id = db.Column(db.Integer, db.ForeignKey("campers.id"))
    snack_id = db.Column(db.Integer, db.ForeignKey("snacks.id"))
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"))
    # Relationships
    camper = db.relationship("Camper", back_populates="lunch_box")
    snack = db.relationship("Snack", back_populates="lunch_box")
    drink = db.relationship("Drink", back_populates="lunch_box")
    # Serialize Rules
    serialize_rules = (
        "-created",
        "-updated",
        "-camper.lunch_box",
        "-snack.lunch_box",
        "-drink.lunch_box",
    )

    # Validations
    @validates("image")
    def validate_image(self, key, image):
        if not image:
            raise ValueError("Image is required for Lunchbox")
        return image

    # __repr__
    def __repr__(self):
        return f"<Lunchbox: {self.id}>"


class Snack(db.Model, SerializerMixin):
    __tablename__ = "snacks"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    name = db.Column(db.String, unique=True, nullable=False)
    image = db.Column(db.String, nullable=False)
    # Relationships
    lunch_box = db.relationship(
        "Lunchbox", back_populates="snack", cascade="all, delete-orphan"
    )
    # Association Proxy
    camper = association_proxy("lunch_box", "camper")
    # Serialize Rules
    serialize_rules = ("-created", "-updated", "-lunch_box.snack")

    # Validations
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Snack name is required")
        elif Snack.query.filter(Snack.name == name).first():
            raise ValueError("Snack name must be unique")
        else:
            return name

    @validates("image")
    def validate_image(self, key, image):
        if not image:
            raise ValueError("Snack image is required")
        return image

    # __repr__
    def __repr__(self):
        return f"<Snack {self.name}>"


class Drink(db.Model, SerializerMixin):
    __tablename__ = "drinks"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    name = db.Column(db.String, unique=True)
    image = db.Column(db.String, nullable=False)
    # Relationships
    lunch_box = db.relationship(
        "Lunchbox", back_populates="drink", cascade="all, delete-orphan"
    )
    # Association Proxy
    camper = association_proxy("lunch_box", "camper")
    # Serialize Rules
    serialize_rules = ("-created", "-updated", "-lunch_box.drink")

    # Validations
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Drink name is required")
        elif Drink.query.filter(Drink.name == name).first():
            raise ValueError("Drink name must be unique")
        else:
            return name

    @validates("image")
    def validate_image(self, key, image):
        if not image:
            raise ValueError("Drink image is required")
        return image

    # __repr__
    def __repr__(self):
        return f"<Drink {self.name}>"


class TreasureChest(db.Model, SerializerMixin):
    __tablename__ = "treasure_chests"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    image = db.Column(db.String, nullable=False)
    # Foreign Key(s)
    camper_id = db.Column(db.Integer, db.ForeignKey("campers.id"))

    # Relationships
    camper = db.relationship("Camper", back_populates="treasure_chest")
    prizes = db.relationship(
        "Prize", back_populates="treasure_chest", cascade="all, delete-orphan"
    )
    # Serialize Rules
    serialize_rules = (
        "-created",
        "-updated",
        "-camper.treasure_chest",
        "-prizes.treasure_chest",
    )

    # Validations
    @validates("image")
    def validate_image(self, key, image):
        if not image:
            raise ValueError("Treasure chest image is required")
        return image

    # __repr__
    def __repr__(self):
        return f"<TreasureChest: {self.id}>"


class Prize(db.Model, SerializerMixin):
    __tablename__ = "prizes"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    token_price = db.Column(db.Integer, nullable=False)
    # Foreign Key(s)
    treasure_chest_id = db.Column(db.Integer, db.ForeignKey("treasure_chests.id"))
    # Relationships
    treasure_chest = db.relationship("TreasureChest", back_populates="prizes")
    # Association Proxy
    campers = association_proxy("treasure_chest", "camper")
    # Serialize Rules
    serialize_rules = ("-created", "-updated", "-treasure_chest.prizes")

    # Validations
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Prize name is required")
        return name

    @validates("image")
    def validate_image(self, key, image):
        if not image:
            raise ValueError("Prize image is required")
        return image

    @validates("token_price")
    def validate_image(self, key, token_price):
        if not token_price:
            raise ValueError("Token price is required")
        elif not isinstance(token_price, int):
            raise ValueError("Token price must be an integer")
        return token_price

    # __repr__
    def __repr__(self):
        return f"<Prize {self.name}: ${self.token_price}>"


class Game(db.Model, SerializerMixin):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rules = db.Column(db.Text, nullable=False)
    win_status = db.Column(db.Boolean)
    image1 = db.Column(db.String, nullable=False)
    image2 = db.Column(db.String)
    image3 = db.Column(db.String)
    image4 = db.Column(db.String)
    # Foreign Key(s)
    camper_id = db.Column(db.Integer, db.ForeignKey("campers.id"))
    token_id = db.Column(db.Integer, db.ForeignKey("tokens.id"))
    # Relationship

    camper = db.relationship("Camper", back_populates="games")
    tokens = db.relationship("Token", back_populates="game")
    # Serialize rules
    serialize_rules = ("-created", "-updated", "-camper.games", "-tokens.game")

    # Validations
    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Game name is required")
        return name

    @validates("description")
    def validate_name(self, key, description):
        if not description:
            raise ValueError("Game description name is required")
        return description

    @validates("rules")
    def validate_name(self, key, rules):
        if not rules:
            raise ValueError("Game rules are required")
        return rules

    @validates("image1")
    def validate_name(self, key, image1):
        if not image1:
            raise ValueError("Game image 1 is required")
        return image1

    # __repr__
    def __repr__(self):
        return f"<Game {self.name}>"


class Token(db.Model, SerializerMixin):
    __tablename__ = "tokens"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    image = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=0)
    # Relationships
    game = db.relationship(
        "Game", back_populates="tokens", cascade="all, delete-orphan"
    )
    # Association Proxy
    camper = association_proxy("game", "camper")
    # Serialize Rules
    serialize_rules = ("-created", "-updated", "-game.tokens")

    # Validations
    @validates("image")
    def validate_name(self, key, image):
        if not image:
            raise ValueError("Token image is required")
        return image

    @validates("amount")
    def validate_name(self, key, amount):
        if not amount:
            raise ValueError("Token amount is required")
        elif not isinstance(amount, int):
            raise ValueError("Token amount must be an integer")
        return amount

    # __repr__
    def __repr__(self):
        return f"<Token {self.amount}>"


class CampfireStory(db.Model, SerializerMixin):
    __tablename__ = "campfire_stories"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image1 = db.Column(db.String, nullable=False)
    image2 = db.Column(db.String)
    image3 = db.Column(db.String)
    # Serialize Rules
    serialize_rules = ("-created", "-updated")

    # Validations
    @validates("title")
    def validate_name(self, key, title):
        if not title:
            raise ValueError("Campfire story title is required")
        elif CampfireStory.query.filter(CampfireStory.title == title).first():
            raise ValueError("Campfire story title must be unique")
        else:
            return title

    @validates("image1")
    def validate_name(self, key, image1):
        if not image1:
            raise ValueError("Campfire Story image1 is required")
        return image1

    @validates("description")
    def validate_name(self, key, description):
        if not description:
            raise ValueError("Campfire story description name is required")
        return description

    # __repr__
    def __repr__(self):
        return f"<CampfireStory {self.title}>"
