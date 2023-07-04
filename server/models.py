from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db


class Camper(db.Model, SerializerMixin):
    __tablename__ = "campers"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    username = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)
    camper_name = db.Column(db.String, unique=True)
    image = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text, nullable=False)
    # Relationships
    lunch_box = db.relationship(
        "Lunchbox", back_populates="camper", cascade="all, delete-orphan"
    )
    treasure_chest = db.relationship(
        "TreasureChest", back_populates="camper", cascade="all, delete-orphan"
    )
    piggy_bank = db.relationship(
        "PiggyBank", back_populates="camper", cascade="all, delete-orphan"
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
    # Validations


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
    prizes = db.relationship("Prize", back_populates="treasure_chest")
    # Association Proxy

    # Serialize Rules
    # Validations


class Prize(db.Model, SerializerMixin):
    __tablename__ = "prizes"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    name = db.Column(db.String, nullabe=False)
    image = db.Column(db.String, nullable=False)
    token_price = db.Column(db.Integer, nullable=False)
    # Foreign Key(s)
    treasure_chest_id = db.Column(db.Integer, db.ForeignKey("treasure_chests.id"))
    # Relationships
    treasure_chest = db.relationship("TreasureChest", back_populates="prizes")
    # Association Proxy
    campers = association_proxy("treasure_chest", "camper")
    # Serialize Rules
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
    camper_win = db.Column(db.Boolean)
    image1 = db.Column(db.String, nullable=False)
    image2 = db.Column(db.String, nullable=False)
    image3 = db.Column(db.String, nullable=False)
    image4 = db.Column(db.String, nullable=False)
    # Foreign Key(s)
    camper_id = db.Column(db.Integer, db.ForeignKey("campers.id"))
    # Relationship

    camper = db.relationship(
        "Camper", back_populates="games", cascade="all, delete-orphan"
    )
    tokens = db.relationship("Token", back_populates="game")
    # Validations
    # Serialize rules


class Token(db.Model, SerializerMixin):
    __tablename__ = "tokens"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    image = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False, default=0)
    # Foreign Key(s)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"))
    # Relationships
    game = db.relationship(
        "Game", back_populates="tokens", cascade="all, delete-orphan"
    )
    # Association Proxy
    camper = association_proxy("game", "camper")
    # Serialize Rules
    # Validations


class CampfireStories(db.Model, SerializerMixin):
    __tablename__ = "campfire_stories"
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    updated = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    title = db.Column(db.String)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    # Serialize Rules
