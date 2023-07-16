import UserContext from "../context/UserContext";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";

function Snack({ snack }) {
  const { user } = useContext(UserContext);
  const navigate = useNavigate();

  function addSnack() {
    fetch(`http://127.0.0.1:5555/lunch_boxes/${user.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ snack_id: snack.id }),
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
      <h4>{snack.name}</h4>
      <img
        className="shadow-xl rounded-md  shadow-neutral-400"
        src={snack.image}
        alt={snack.name}
        style={{
          width: 160,
          borderBottomLeftRadius: 0,
          borderBottomRightRadius: 0,
        }}
      />
      <button
        className="bg-neutral-100 hover:bg-yellow-300 rounded-md py-2 shadow-xl text-xs uppercase tracking-widest"
        style={{
          borderTopLeftRadius: 0,
          borderTopRightRadius: 0,
          width: "160px",
        }}
        onClick={addSnack}
      >
        Add to Lunchbox
      </button>
    </div>
  );
}

export default Snack;
