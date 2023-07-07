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
from faker import Faker

fake = Faker()


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

    # ------------------------------------------------------------|
    # TOKENS
    # ------------------------------------------------------------|

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
    # ------------------------------------------------------------|
    # CAMPERS
    # ------------------------------------------------------------|

    camper1 = Camper(
        username="Billy87",
        _password_hash="sndfuh89r3rfn3",
        camper_name="Billy",
        image="https://images.unsplash.com/photo-1566492031773-4f4e44671857?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGJsYWNrJTIwbWFufGVufDB8fDB8fHww&auto=format&fit=crop&w=700&q=60",
        bio="NFL loving buy from the deep south. I love the Carolina Panthers. 'Go, Carolina!'",
    )
    camper2 = Camper(
        username="nadia111",
        _password_hash="sn234rh2fd3",
        camper_name="Nadia",
        image="https://images.unsplash.com/photo-1544714042-5c0a53d63ed5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTZ8fGJsYWNrJTIwd29tYW58ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=700&q=60",
        bio="Ethiopian born, American made. I love music, shopping, and hanging with friends",
    )
    camper3 = Camper(
        username="tasha1998",
        _password_hash="sndfuh24333rfn3",
        camper_name="Natasha",
        image="https://images.unsplash.com/photo-1616002411355-49593fd89721?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fHdvbWFuJTIwZmFjZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=700&q=60",
        bio="Hi, I'm Natasha, I love reading and drawing",
    )
    camper4 = Camper(
        username="jwon4539",
        _password_hash="sndfuh32443243",
        camper_name="Jayson",
        image="https://images.unsplash.com/photo-1611459293885-f8e692ab0356?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fGFzaWFuJTIwbWFufGVufDB8fDB8fHww&auto=format&fit=crop&w=700&q=60",
        bio="What's up! I'm Jayson. Love to play video games, and hit every music festival I can",
    )
    camper5 = Camper(
        username="amna35011",
        _password_hash="sndf342432fn3",
        camper_name="Amna",
        image="https://images.unsplash.com/photo-1500060257085-312ef9591798?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fGFyYWJpYyUyMHdvbWFufGVufDB8fDB8fHww&auto=format&fit=crop&w=700&q=60",
        bio="I love being outside. I love gardening and hanging with my friends and family",
    )

    campers = [camper1, camper2, camper3, camper4, camper5]
    db.session.add_all(campers)
    # ------------------------------------------------------------|
    # GAMES
    # ------------------------------------------------------------|
    game1 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=True,
        image1=fake.name(),
        camper=choice(campers),
        tokens=choice(tokens),
    )
    game2 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=False,
        image1=fake.name(),
        camper=choice(campers),
        tokens=choice(tokens),
    )
    game3 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=False,
        image1=fake.name(),
        camper=choice(campers),
        tokens=choice(tokens),
    )
    game4 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=True,
        image1=fake.name(),
        camper=choice(campers),
        tokens=choice(tokens),
    )
    game5 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=True,
        image1=fake.name(),
        camper=choice(campers),
        tokens=choice(tokens),
    )

    games = [game1, game2, game3, game4, game5]
    db.session.add_all(games)
    # ------------------------------------------------------------|
    # SNACKS
    # ------------------------------------------------------------|

    snack1 = Snack(
        name="DunkAroos",
        image="https://www.gosupps.com/media/catalog/product/cache/25/image/1500x/040ec09b1e35df139433887a97daa66f/9/1/91wYzJzS0YS._SL1500_.jpg",
    )
    snack2 = Snack(
        name="Oreo Minis", image="https://cdnimages.opentip.com/full/DOF/DOF-449011.jpg"
    )
    snack3 = Snack(
        name="Lunchables - Turkey & Cheddar",
        image="https://www.kroger.com/product/images/large/front/0004470002455",
    )

    snacks = [snack1, snack2, snack3]
    db.session.add_all(snacks)
    # ------------------------------------------------------------|
    # DRINKS
    # ------------------------------------------------------------|
    drink1 = Drink(
        name="Capri Sun Fruit Punch",
        image="https://d3ldzx7fxfvsfy.cloudfront.net/233/studio/assets/v1687961059496_95364841/CS-FruitPunch-Updated.png",
    )
    drink2 = Drink(
        name="Mott's Apple Juice",
        image="https://m.media-amazon.com/images/I/71qosBESVVL.jpg",
    )
    drink3 = Drink(
        name="Tropicana Orange Juice",
        image="https://www.webstaurantstore.com/images/products/landscape/702357/2419030.jpg",
    )

    drinks = [drink1, drink2, drink3]
    db.session.add_all(drinks)

    # ------------------------------------------------------------|
    # LUNCH BOXES
    # ------------------------------------------------------------|

    lunchbox1 = Lunchbox(
        image=fake.name(),
        camper=choice(campers),
        snack=choice(snacks),
        drink=choice(drinks),
    )
    lunchbox2 = Lunchbox(
        image=fake.name(),
        camper=choice(campers),
        snack=choice(snacks),
        drink=choice(drinks),
    )
    lunchbox3 = Lunchbox(
        image=fake.name(),
        camper=choice(campers),
        snack=choice(snacks),
        drink=choice(drinks),
    )

    lunch_boxes = [lunchbox1, lunchbox2, lunchbox3]
    db.session.add_all(lunch_boxes)
    # ------------------------------------------------------------|
    # TREASURES
    # ------------------------------------------------------------|

    treasure1 = TreasureChest(
        image="https://as2.ftcdn.net/v2/jpg/05/52/07/15/1000_F_552071588_8YeH0HA0dBPL1LNX7Gf069muLwbfOEnj.jpg",
        camper=camper1,
    )
    treasure2 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        camper=camper2,
    )
    treasure3 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        camper=camper3,
    )
    treasure4 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        camper=camper4,
    )
    treasure5 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        camper=camper5,
    )
    treasures = [treasure1, treasure2, treasure3, treasure4, treasure5]
    db.session.add_all(treasures)
    # ------------------------------------------------------------|
    # PRIZES
    # ------------------------------------------------------------|
    prize1 = Prize(
        name=fake.name(),
        image=fake.name(),
        token_price=10,
        treasure_chest=choice(treasures),
    )
    prize2 = Prize(
        name=fake.name(),
        image=fake.name(),
        token_price=10,
        treasure_chest=choice(treasures),
    )
    prize3 = Prize(
        name=fake.name(),
        image=fake.name(),
        token_price=15,
        treasure_chest=choice(treasures),
    )
    prize4 = Prize(
        name=fake.name(),
        image=fake.name(),
        token_price=20,
        treasure_chest=choice(treasures),
    )
    prize5 = Prize(
        name=fake.name(),
        image=fake.name(),
        token_price=30,
        treasure_chest=choice(treasures),
    )
    prize6 = Prize(
        name=fake.name(),
        image=fake.name(),
        token_price=50,
    )

    prizes = [prize1, prize2, prize3, prize4, prize5, prize6]
    db.session.add_all(prizes)

    # ------------------------------------------------------------|
    # CAMPFIRE STORIES
    # ------------------------------------------------------------|

    story1 = CampfireStory(title="Story1", image1=fake.name(), description=fake.text())
    story2 = CampfireStory(title="Story2", image1=fake.name(), description=fake.text())
    story3 = CampfireStory(title="Story3", image1=fake.name(), description=fake.text())
    story4 = CampfireStory(title="Story4", image1=fake.name(), description=fake.text())
    story5 = CampfireStory(title="Story5", image1=fake.name(), description=fake.text())

    stories = [story1, story2, story3, story4, story5]
    db.session.add_all(stories)

    # ---------------------------------------------------------
    db.session.commit()
    print("Done Seeding!")
