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
    <div>
      <h4>{snack.name}</h4>
      <img src={snack.image} style={{ width: 200, borderRadius: "20px" }} />
      <button onClick={addSnack}>Add to Lunchbox</button>
    </div>
  );
}

export default Snack;
