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
    <div style={{ display: "inline-block" }} className="hover:scale-110">
      <h4>{snack.name}</h4>
      <img
        className="shadow-xl rounded-3xl"
        src={snack.image}
        style={{ width: 160, paddingLeft: "10px" }}
      />
      <button
        className="bg-yellow-400 hover:bg-yellow-300 rounded-3xl py-2 px-6 shadow-xl text-xs uppercase"
        onClick={addSnack}
      >
        Add to Lunchbox
      </button>
    </div>
  );
}

export default Snack;
