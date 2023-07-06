from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db
from config import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class Camper(db.Model, SerializerMixin):
    __tablename__ = "campers"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    camper_name = db.Column(db.String)
    image = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text, nullable=False)
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

    # __repr__
    def __repr__(self):
        return f"<Lunchbox: {self.id}>"

    # Validations


class Snack(db.Model, SerializerMixin):
    __tablename__ = "snacks"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    name = db.Column(db.String, unique=True)
    image = db.Column(db.String, nullable=False)
    # Relationships
    lunch_box = db.relationship(
        "Lunchbox", back_populates="snack", cascade="all, delete-orphan"
    )
    # Association Proxy
    camper = association_proxy("lunch_box", "camper")
    # Serialize Rules
    serialize_rules = ("-created", "-updated", "-lunch_box.snack")

    # __repr__
    def __repr__(self):
        return f"<Snack {self.name}>"

    # Validations


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

    # __repr__
    def __repr__(self):
        return f"<Drink {self.name}>"

    # Validations


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

    # __repr__
    def __repr__(self):
        return f"<TreasureChest: {self.id}>"

    # Validations


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

    # __repr__
    def __repr__(self):
        return f"<Prize {self.name}: ${self.token_price}>"

    # Validations


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

    # __repr__
    def __repr__(self):
        return f"<Game {self.name}>"

    # Validations


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

    # __repr__
    def __repr__(self):
        return f"<Token {self.amount}>"

    # Validations


class CampfireStory(db.Model, SerializerMixin):
    __tablename__ = "campfire_stories"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    title = db.Column(db.String)
    description = db.Column(db.Text, nullable=False)
    image1 = db.Column(db.String, nullable=False)
    image2 = db.Column(db.String)
    image3 = db.Column(db.String)
    # Serialize Rules
    serialize_rules = ("-created", "-updated")

    # __repr__
    def __repr__(self):
        return f"<CampfireStory {self.title}>"
