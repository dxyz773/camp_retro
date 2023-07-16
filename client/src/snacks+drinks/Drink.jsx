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
    <div
      style={{
        width: "200px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
      className="hover:scale-105"
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
        className="bg-neutral-100 hover:bg-yellow-300 rounded-md py-2 shadow-xl text-xs uppercase tracking-widest"
        style={{
          borderTopLeftRadius: 0,
          borderTopRightRadius: 0,
          width: "160px",
        }}
        onClick={addDrink}
      >
        Add to Lunchbox
      </button>
    </div>
  );
}

export default Drink;
