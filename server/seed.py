from config import app, db
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
from random import choice

with app.app_context():
    print("Begin Seeding...")

    Camper.query.delete()
    Lunchbox.query.delete()
    Snack.query.delete()
    Drink.query.delete()
    TreasureChest.query.delete()
    Prize.query.delete()
    Game.query.delete()
    Token.query.delete()
    CampfireStory.query.delete()

    token1 = Token(
        image="https://m.media-amazon.com/images/I/6157nGy5RLL._AC_SL1000_.jpg",
        amount=10,
    )
    token2 = Token(
        image="https://m.media-amazon.com/images/I/6157nGy5RLL._AC_SL1000_.jpg",
        amount=15,
    )
    token3 = Token(
        image="https://m.media-amazon.com/images/I/6157nGy5RLL._AC_SL1000_.jpg",
        amount=20,
    )
    token4 = Token(
        image="https://m.media-amazon.com/images/I/6157nGy5RLL._AC_SL1000_.jpg",
        amount=30,
    )
    token5 = Token(
        image="https://m.media-amazon.com/images/I/6157nGy5RLL._AC_SL1000_.jpg",
        amount=50,
    )

    tokens = [token1, token2, token3, token4, token5]
    db.session.add_all(tokens)

    camper1 = Camper(
        username="Billy87",
        _password_hash="sndfuh89r3rfn3",
        camper_name="Billy",
        image="",
        bio="NFL loving buy from the deep south. I love the Carolina Panthers. 'Go, Carolina!'",
    )
    camper2 = Camper(
        username="nadia111",
        _password_hash="sn234rh2fd3",
        camper_name="Nadia",
        image="",
        bio="Ethiopian born, American made. I love music, shopping, and hanging with friends",
    )
    camper3 = Camper(
        username="tasha1998",
        _password_hash="sndfuh24333rfn3",
        camper_name="Natasha",
        image="",
        bio="Hi, I'm Natasha, I love reading and drawing",
    )
    camper4 = Camper(
        username="jwon4539",
        _password_hash="sndfuh32443243",
        camper_name="Jayson",
        image="",
        bio="What's up! I'm Jayson. Love to play video games, and hit every music festival I can",
    )
    camper5 = Camper(
        username="amna35011",
        _password_hash="sndf342432fn3",
        camper_name="Amna",
        image="",
        bio="I love being outside. I love gardening and hanging with my friends and family",
    )

    campers = [camper1, camper2, camper3, camper4, camper5]

    db.session.add_all(campers)
    treasure1 = TreasureChest(
        image="https://as2.ftcdn.net/v2/jpg/05/52/07/15/1000_F_552071588_8YeH0HA0dBPL1LNX7Gf069muLwbfOEnj.jpg",
        camper=choice(campers),
    )
    treasure2 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        camper=choice(campers),
    )
    treasures = [treasure1, treasure2]
    db.session.add_all(treasures)

    story1 = CampfireStory(title="Story1", image1="", description="Story1")
    story2 = CampfireStory(title="Story2", image1="", description="Story2")
    story3 = CampfireStory(title="Story3", image1="", description="Story3")
    story4 = CampfireStory(title="Story4", image1="", description="Story4")
    story5 = CampfireStory(title="Story5", image1="", description="Story5")

    print("Done Seeding!")
