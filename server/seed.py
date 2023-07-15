from config import app, db
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
from random import choice
from faker import Faker

fake = Faker()


with app.app_context():
    print("Begin Seeding...")

    User.query.delete()
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
    # USERS
    # ------------------------------------------------------------|

    user1 = User(
        username="Billy87",
        _password_hash="sndfuh89r3rfn3",
        camper_name="Billy",
        image="https://images.unsplash.com/photo-1566492031773-4f4e44671857?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGJsYWNrJTIwbWFufGVufDB8fDB8fHww&auto=format&fit=crop&w=700&q=60",
        bio="NFL loving buy from the deep south. I love the Carolina Panthers. 'Go, Carolina!'",
    )
    user2 = User(
        username="nadia111",
        _password_hash="sn234rh2fd3",
        camper_name="Nadia",
        image="https://images.unsplash.com/photo-1544714042-5c0a53d63ed5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTZ8fGJsYWNrJTIwd29tYW58ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=700&q=60",
        bio="Ethiopian born, American made. I love music, shopping, and hanging with friends",
    )
    user3 = User(
        username="tasha1998",
        _password_hash="sndfuh24333rfn3",
        camper_name="Natasha",
        image="https://images.unsplash.com/photo-1616002411355-49593fd89721?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fHdvbWFuJTIwZmFjZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=700&q=60",
        bio="Hi, I'm Natasha, I love reading and drawing",
    )
    user4 = User(
        username="jwon4539",
        _password_hash="sndfuh32443243",
        camper_name="Jayson",
        image="https://images.unsplash.com/photo-1611459293885-f8e692ab0356?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fGFzaWFuJTIwbWFufGVufDB8fDB8fHww&auto=format&fit=crop&w=700&q=60",
        bio="What's up! I'm Jayson. Love to play video games, and hit every music festival I can",
    )
    user5 = User(
        username="amna35011",
        _password_hash="sndf342432fn3",
        camper_name="Amna",
        image="https://images.unsplash.com/photo-1500060257085-312ef9591798?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fGFyYWJpYyUyMHdvbWFufGVufDB8fDB8fHww&auto=format&fit=crop&w=700&q=60",
        bio="I love being outside. I love gardening and hanging with my friends and family",
    )

    users = [user1, user2, user3, user4, user5]
    db.session.add_all(users)
    # ------------------------------------------------------------|
    # GAMES
    # ------------------------------------------------------------|
    game1 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=True,
        image1=fake.name(),
        user=choice(users),
        tokens=choice(tokens),
    )
    game2 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=False,
        image1=fake.name(),
        user=choice(users),
        tokens=choice(tokens),
    )
    game3 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=False,
        image1=fake.name(),
        user=choice(users),
        tokens=choice(tokens),
    )
    game4 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=True,
        image1=fake.name(),
        user=choice(users),
        tokens=choice(tokens),
    )
    game5 = Game(
        name=fake.name(),
        description=fake.text(),
        rules=fake.text(),
        win_status=True,
        image1=fake.name(),
        user=choice(users),
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
    snack4 = Snack(
        name="Red Apple",
        image="https://www.applesfromny.com/wp-content/uploads/2020/06/SnapdragonNEW.png",
    )
    snack5 = Snack(
        name="Green Apple",
        image="https://i.etsystatic.com/13808628/r/il/b63d4a/3424214067/il_1588xN.3424214067_2qtg.jpg",
    )
    snack6 = Snack(
        name="Ritz Crackers",
        image="https://ipcdn.freshop.com/resize?url=https://images.freshop.com/00044000002114/a46d0dda800797e31bdb773e402d809e_large.png&width=512&type=webp&quality=90",
    )
    snack7 = Snack(
        name="Welch's Mixed Fruit Snack",
        image="https://target.scene7.com/is/image/Target/GUEST_e6aaeac9-30f8-4057-a510-552e6463c78b?wid=1000&hei=1000&qlt=80&fmt=webp",
    )
    snack7 = Snack(
        name="Goldfish",
        image="https://target.scene7.com/is/image/Target/GUEST_83d12fba-168b-405d-8310-5a621da4648b?wid=1000&hei=1000&qlt=80&fmt=webp",
    )
    snack8 = Snack(
        name="Watermelon Slice",
        image="https://img.freepik.com/premium-psd/sliced-watermelon-isolated-white_253984-6008.jpg",
    )
    snack9 = Snack(
        name="String Cheese",
        image="https://i5.walmartimages.com/asr/ff61d3de-ae40-4b4d-99e6-8957865e323c.69831eabbccd5543d6ca8471ba954b86.jpeg?odnHeight=2000&odnWidth=2000&odnBg=FFFFFF",
    )
    snack10 = Snack(
        name="Rice Krispies Treats",
        image="https://kellogg-h.assetsadobe.com/is/image/content/dam/kelloggs/kna/us/digital-shelf/rice-krispies-treats/00038000110528_C1NB.jpg",
    )

    snacks = [
        snack1,
        snack2,
        snack3,
        snack4,
        snack5,
        snack6,
        snack7,
        snack8,
        snack9,
        snack10,
    ]
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
    drink4 = Drink(
        name="Blueberry Smoothe",
        image="https://assets.bonappetit.com/photos/63a1e0b3c37a58ec105a304e/1:1/w_2560%2Cc_limit/1220-smoothie-blueberry-lede.jpg",
    )
    drink5 = Drink(
        name="Mango Juicebox",
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCf_JN_TBDhPomXI7uFFy57-VZ-Esm_18jt5xNdKYyzEWU15DcLz9ETkXI2dAP6-FuCFE&usqp=CAU",
    )
    drink6 = Drink(
        name="Strawberry Smoothie",
        image="https://www.dinneratthezoo.com/wp-content/uploads/2018/05/strawberry-banana-smoothie-4.jpg",
    )
    drink7 = Drink(
        name="Chocolate Yoohoo",
        image="https://bagelsyourwaycafe.com/wp-content/uploads/2021/05/Yoo-Hoo-Glass-Bottle_640x360.jpg",
    )
    drink8 = Drink(
        name="Grape Kool-Aid Jammers",
        image="https://i5.walmartimages.com/asr/58543e52-8298-4027-91f4-549782ec74c6_1.86bb6330b226e0960867f2c7e30e0339.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    )
    drink9 = Drink(
        name="Cherry Kool-Aid Jammers",
        image="https://i5.walmartimages.com/asr/c42880be-e165-4d37-a86c-4b6a0abacf4a_1.34e439c702d4ba0bce4e5de80287e124.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    )
    drink10 = Drink(
        name="Tropical Punch Kool-Aid Jammers",
        image="https://www.foodservicedirect.com/media/catalog/product/0/0/00043000047293_ws_2_8jpvuhy2jkufgpxy.jpg?width=1200&height=1200&quality=85&fit=bounds",
    )

    drinks = [
        drink1,
        drink2,
        drink3,
        drink4,
        drink5,
        drink6,
        drink7,
        drink8,
        drink9,
        drink10,
    ]
    db.session.add_all(drinks)

    # ------------------------------------------------------------|
    # LUNCH BOXES
    # ------------------------------------------------------------|

    lunchbox1 = Lunchbox(
        image="https://buyrocknroll.rocks/cdn/shop/products/c61284d5-d092-5772-893c-5753c244ea31_1000x.jpg?v=1552155505",
        user_id=1,
        snack=choice(snacks),
        drink=choice(drinks),
    )
    lunchbox2 = Lunchbox(
        image="https://buyrocknroll.rocks/cdn/shop/products/c61284d5-d092-5772-893c-5753c244ea31_1000x.jpg?v=1552155505",
        user_id=2,
        snack=choice(snacks),
        drink=choice(drinks),
    )
    lunchbox3 = Lunchbox(
        image="https://buyrocknroll.rocks/cdn/shop/products/c61284d5-d092-5772-893c-5753c244ea31_1000x.jpg?v=1552155505",
        user_id=3,
        snack=choice(snacks),
        drink=choice(drinks),
    )
    lunchbox4 = Lunchbox(
        image="https://buyrocknroll.rocks/cdn/shop/products/c61284d5-d092-5772-893c-5753c244ea31_1000x.jpg?v=1552155505",
        user_id=4,
        snack=choice(snacks),
        drink=choice(drinks),
    )
    lunchbox5 = Lunchbox(
        image="https://buyrocknroll.rocks/cdn/shop/products/c61284d5-d092-5772-893c-5753c244ea31_1000x.jpg?v=1552155505",
        user_id=5,
        snack=choice(snacks),
        drink=choice(drinks),
    )

    lunch_boxes = [lunchbox1, lunchbox2, lunchbox3, lunchbox4, lunchbox5]
    db.session.add_all(lunch_boxes)
    # ------------------------------------------------------------|
    # TREASURES
    # ------------------------------------------------------------|

    treasure1 = TreasureChest(
        image="https://as2.ftcdn.net/v2/jpg/05/52/07/15/1000_F_552071588_8YeH0HA0dBPL1LNX7Gf069muLwbfOEnj.jpg",
        user=user1,
    )
    treasure2 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        user=user2,
    )
    treasure3 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        user=user3,
    )
    treasure4 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        user=user4,
    )
    treasure5 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        user=user5,
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
