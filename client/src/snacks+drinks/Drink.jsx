import UserContext from "../context/UserContext";
import { useContext, useState } from "react";

function Drink({ drink }) {
  const { user } = useContext(UserContext);
  const [message, setMessage] = useState("");

  function addDrink() {
    fetch(`http://127.0.0.1:5555/lunch_boxes/${user.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ drink_id: drink.id }),
    }).then(() => setMessage("ADDED!"));
  }
  return (
    <div
      style={{ width: "200px" }}
      className="hover:scale-105 transition-all duration-200 flex flex-col items-center"
    >
      <h4>{drink.name}</h4>
      <img
        src={drink.image}
        className="shadow-xl rounded-md  shadow-neutral-400"
        style={{
          width: 160,
          borderBottomLeftRadius: 0,
          borderBottomRightRadius: 0,
        }}
        alt={drink.name}
      />
      <button
        className="bg-neutral-100 hover:bg-yellow-300 rounded-md py-2 shadow-xl text-xs uppercase tracking-widest transition-all duration-300"
        style={{
          borderTopLeftRadius: 0,
          borderTopRightRadius: 0,
          width: "160px",
        }}
        onClick={addDrink}
      >
        {message ? message : "Add to Lunchbox"}
      </button>
    </div>
  );
}

export default Drink;
