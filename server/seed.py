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
        bio="Hey everyone, I'm Nadia. I love music, shopping, and hanging with friends",
    )
    user3 = User(
        username="tasha1998",
        _password_hash="sndfuh24333rfn3",
        camper_name="Natasha",
        image="https://images.unsplash.com/photo-1616002411355-49593fd89721?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTd8fHdvbWFuJTIwZmFjZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=700&q=60",
        bio="Hi, I'm Natasha, I love reading and drawing.",
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
    user6 = User(
        username="Amy205311",
        _password_hash="snsdsdfds222",
        camper_name="Amy",
        image="https://images.unsplash.com/photo-1521227889351-bf6f5b2e4e37?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1325&q=80",
        bio="Hey, I'm Amy! I am all about music festivals and art galleries!",
    )
    user7 = User(
        username="JonaMTexas555",
        _password_hash="sns5555522",
        camper_name="Jona",
        image="https://images.unsplash.com/photo-1463453091185-61582044d556?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80",
        bio="I'm Jona. Into anime, gaming, and fashion",
    )
    users = [user1, user2, user3, user4, user5, user6, user7]
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
        name="Lunchables",
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
    snack11 = Snack(
        name="Blueberry Nutrigrain",
        image="https://mountainmerchantvt.com/wp-content/uploads/2019/06/nutriblue.jpg",
    )
    snack12 = Snack(
        name="Berry Nutrigrain",
        image="https://kellogg-h.assetsadobe.com/is/image/content/dam/kelloggs/kna/us/digital-shelf/nutri-grain-bars/00038000597725_C1N1.jpg",
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
        snack11,
        snack12,
    ]
    db.session.add_all(snacks)
    # ------------------------------------------------------------|
    # DRINKS
    # ------------------------------------------------------------|
    drink1 = Drink(
        name="Hawaiian Punch",
        image="https://www.kroger.com/product/images/large/right/0001480000371",
    )
    drink2 = Drink(
        name="Mott's Apple Juice",
        image="https://m.media-amazon.com/images/I/71qosBESVVL.jpg",
    )
    drink3 = Drink(
        name="Orange Juice",
        image="https://ipcdn.freshop.com/resize?url=https://images.freshop.com/00048500018521/0b6093f1ffad4c7865fcc60457d6bf3e_large.png&width=512&type=webp&quality=90",
    )
    drink4 = Drink(
        name="Blueberry Smoothe",
        image="https://assets.bonappetit.com/photos/63a1e0b3c37a58ec105a304e/1:1/w_2560%2Cc_limit/1220-smoothie-blueberry-lede.jpg",
    )
    drink5 = Drink(
        name="Grape Juice",
        image="https://grocerylistjamaica.com/wp-content/uploads/2021/11/Juicy-Juice-100-Juice-Grape-200Ml.jpg",
    )
    drink6 = Drink(
        name="Strawberry Smoothie",
        image="https://www.liveeatlearn.com/wp-content/uploads/2019/08/strawberry-smoothie-photo-vert.jpg",
    )
    drink7 = Drink(
        name="Chocolate Yoohoo",
        image="https://storage.googleapis.com/images-cub-prd-9400d55.cub.prd.v8.commerce.mi9cloud.com/product-images/zoom/12658151-61f1-4729-9dc9-8d655d1d0b33.jpeg",
    )
    drink8 = Drink(
        name="Grape Kool-Aid",
        image="https://i5.walmartimages.com/asr/58543e52-8298-4027-91f4-549782ec74c6_1.86bb6330b226e0960867f2c7e30e0339.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    )
    drink9 = Drink(
        name="Cherry Kool-Aid",
        image="https://i5.walmartimages.com/asr/c42880be-e165-4d37-a86c-4b6a0abacf4a_1.34e439c702d4ba0bce4e5de80287e124.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    )
    drink10 = Drink(
        name="Tropical Kool-Aid",
        image="https://www.foodservicedirect.com/media/catalog/product/0/0/00043000047293_ws_2_8jpvuhy2jkufgpxy.jpg?width=1200&height=1200&quality=85&fit=bounds",
    )
    drink11 = Drink(
        name="Minute Maid Lemonade ",
        image="https://m.media-amazon.com/images/I/41hIb4QDivL._SX300_SY300_QL70_FMwebp_.jpg",
    )
    drink12 = Drink(
        name="Sweet Tea",
        image="https://sugarspunrun.com/wp-content/uploads/2022/05/Easy-sweet-tea-recipe-1-of-1.jpg",
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
        drink11,
        drink12,
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
    lunchbox6 = Lunchbox(
        image="https://buyrocknroll.rocks/cdn/shop/products/c61284d5-d092-5772-893c-5753c244ea31_1000x.jpg?v=1552155505",
        user_id=6,
        snack=choice(snacks),
        drink=choice(drinks),
    )
    lunchbox7 = Lunchbox(
        image="https://buyrocknroll.rocks/cdn/shop/products/c61284d5-d092-5772-893c-5753c244ea31_1000x.jpg?v=1552155505",
        user_id=7,
        snack=choice(snacks),
        drink=choice(drinks),
    )

    lunch_boxes = [
        lunchbox1,
        lunchbox2,
        lunchbox3,
        lunchbox4,
        lunchbox5,
        lunchbox6,
        lunchbox7,
    ]
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
    treasure6 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        user=user6,
    )
    treasure7 = TreasureChest(
        image="https://media.istockphoto.com/id/1160778039/photo/treasure-chest-open-ancient-trunk-with-glowing-magic-lights-in-the-dark.jpg?s=612x612&w=0&k=20&c=yMQNCICQAzZQYXK09nTnIzKs22A7j5zLqo-cTkTO134=",
        user=user7,
    )
    treasures = [
        treasure1,
        treasure2,
        treasure3,
        treasure4,
        treasure5,
        treasure6,
        treasure7,
    ]
    db.session.add_all(treasures)
    # ------------------------------------------------------------|
    # PRIZES
    # ------------------------------------------------------------|
    prize1 = Prize(
        name="Grey Beige Furby",
        image="https://i.etsystatic.com/32576510/r/il/c3769e/4891656971/il_1588xN.4891656971_24tf.jpg",
        token_price=60,
        treasure_chest=choice(treasures),
    )
    prize2 = Prize(
        name="Easy Bake Oven",
        image="https://imgix.bustle.com/fatherly/2017/07/easy-bake-oven.png?w=768&h=416&fit=crop&crop=faces&auto=format%2Ccompress&q=50&dpr=2",
        token_price=10,
        treasure_chest=choice(treasures),
    )
    prize3 = Prize(
        name="Polly Pocket Stampin School",
        image="https://i.etsystatic.com/7557985/r/il/2d820b/4547197612/il_1588xN.4547197612_nkod.jpg",
        token_price=15,
        treasure_chest=choice(treasures),
    )
    prize4 = Prize(
        name="Bop it",
        image="https://i0.wp.com/retropond.com/wp-content/uploads/2021/05/BopIt-Featured.jpg?w=1556&ssl=1",
        token_price=20,
        treasure_chest=choice(treasures),
    )
    prize5 = Prize(
        name="Purple Tamagotchi",
        image="https://m.media-amazon.com/images/I/81rkRztLpjL._AC_SL1500_.jpg",
        token_price=30,
        treasure_chest=choice(treasures),
    )
    prize6 = Prize(
        name="Neon Tamagotchi",
        image="https://m.media-amazon.com/images/I/81Z27dmbVbL._AC_SL1500_.jpg",
        token_price=50,
    )
    prize7 = Prize(
        name="White Furby",
        image="https://i.etsystatic.com/27542120/r/il/8c9213/4813277261/il_1588xN.4813277261_elev.jpg",
        token_price=50,
    )
    prize8 = Prize(
        name="Mint Green Furby",
        image="https://i.etsystatic.com/32576510/r/il/30164a/4903191388/il_1588xN.4903191388_qfl4.jpg",
        token_price=50,
    )
    prize9 = Prize(
        name="SONY WALKMAN D-SJ301 PORTABLE CD PLAYER",
        image="https://retrospekt.com/cdn/shop/files/PD-VR-1160_1copy.jpg?v=1685973419&width=3200",
        token_price=80,
    )
    prize10 = Prize(
        name="Nintendo Game Boy",
        image="https://retrospekt.com/cdn/shop/files/og-2_42b7141a-8699-4d4c-8144-e88561ca7d53.jpg?v=1686078109&width=1400",
        token_price=100,
    )

    prizes = [
        prize1,
        prize2,
        prize3,
        prize4,
        prize5,
        prize6,
        prize7,
        prize8,
        prize9,
        prize10,
    ]
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
