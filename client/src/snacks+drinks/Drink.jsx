import UserContext from "../context/UserContext";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";

function Drink({ drink }) {
  const { user } = useContext(UserContext);
  const navigate = useNavigate();

  function addDrink() {
    fetch(`http://127.0.0.1:5555/lunch_boxes/${user.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ drink_id: drink.id }),
    }).then((res) =>
      res.json().then(() => {
        navigate("/lunchbox");
      })
    );
  }
  return (
    <div>
      <h4>{drink.name}</h4>
      <img
        src={drink.image}
        style={{ width: 200, borderRadius: "20px" }}
        alt={drink.name}
      />
      <button onClick={addDrink}>Add to Lunchbox</button>
    </div>
  );
}

export default Drink;
