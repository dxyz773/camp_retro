# 🌲🌖 camp retro 🏕️

### No camp counselors. Just games, prizes, and retro fun.

## ERD

## <img src="images/ERD.png">

---

## API Routes

| API Route             | Request Method | Body                                          | Response                                                                                        |
| --------------------- | -------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| /campers              | GET            |                                               | [{...},{...},...]                                                                               |
| /campers/:id          | GET            |                                               | {id, username, camper_name, image, bio}                                                         |
| /campers/:id          | PATCH          | {username, camper_name, image, bio}           | {id, username, camper_name, image, bio}                                                         |
| /campers/:id          | DELETE         |                                               | {}                                                                                              |
| /lunch_boxes/:id      | GET            |                                               | {id, image, camper_id, snack_id, drink_id}                                                      |
| /lunch_boxes/:id      | PATCH          | {snack_id, drink_id}                          | {id, image, camper_id, snack_id, drink_id}                                                      |
| /snacks               | GET            |                                               | [{...},{...},...]                                                                               |
| /snacks/:id           | GET            |                                               | {id, name, image}                                                                               |
| /drinks               | GET            |                                               | [{...},{...},...]                                                                               |
| /drinks/:id           | GET            |                                               | {id, name, image}                                                                               |
| /treasure_chests/:id  | GET            |                                               | {id, image, camper_id}                                                                          |
| /prizes               | GET            |                                               | [{...},{...},...]                                                                               |
| /prizes/:id           | GET            |                                               | {id, name, image, token_price, treasure_chest_id}                                               |
| /prizes/:id           | PATCH          | {treasure_chest_id}                           | {id, name, image, token_price, treasure_chest_id}                                               |
| /games                | GET            |                                               | [{...},{...},...]                                                                               |
| /games/:id            | GET            |                                               | {id, name, description, rules, win_status, image1, image2, image3, image4, camper_id, token_id} |
| /games/:id            | PATCH          | {camper_id}                                   | {id, name, description, rules, win_status, image1, image2, image3, image4, camper_id, token_id} |
| /tokens/:id           | GET            |                                               | {id, image, amount}                                                                             |
| /campfire_stories     | GET            |                                               | [{...},{...},...]                                                                               |
| /campfire_stories/:id | GET            |                                               | {id, title, description, image1, image2, image3}                                                |
| /login                | POST           | {username, password}                          | {id, name, img, username}                                                                       |
| /signup               | POST           | {username, password, camper_name, image, bio} | {id, username, camper_name, image, bio}                                                         |
| /check_session        | GET            |                                               | {id, name, img, username}                                                                       |
| /logout               | DELETE         |                                               | {}                                                                                              |

---

## trello

<img src="images/Trello.png">
