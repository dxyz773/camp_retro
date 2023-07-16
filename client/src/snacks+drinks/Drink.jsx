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
        className="shadow-xl rounded-3xl"
        style={{ width: 170 }}
        alt={drink.name}
      />
      <button
        className="bg-yellow-400 hover:bg-yellow-300 rounded-3xl py-2 px-6 shadow-xl"
        onClick={addDrink}
      >
        Add to Lunchbox
      </button>
    </div>
  );
}

export default Drink;
