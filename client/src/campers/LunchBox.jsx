import UserContext from "../context/UserContext";
import { useContext, useEffect } from "react";

function LunchBox() {
  const { user, updateUser } = useContext(UserContext);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/check_session")
      .then((res) => res.json())
      .then((data) => updateUser(data));
  }, []);
  return (
    <div>
      <h4>Snack</h4>
      <p>{user.lunch_box[0].snack.name}</p>
      <img
        src={user.lunch_box[0].snack.image}
        alt={user.lunch_box[0].snack.name}
        width={200}
      />
      <h4>Drink</h4>
      <p>{user.lunch_box[0].drink.name}</p>
      <img
        src={user.lunch_box[0].drink.image}
        alt={user.lunch_box[0].drink.name}
        width={200}
      />
    </div>
  );
}

export default LunchBox;
