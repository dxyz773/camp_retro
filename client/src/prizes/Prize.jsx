// import UserContext from "../context/UserContext";
// import { useContext } from "react";
// import { useNavigate } from "react-router-dom";

function Prize({ prize }) {
  // const { user } = useContext(UserContext);
  // const navigate = useNavigate();

  // function addSnack() {
  //   fetch(`http://127.0.0.1:5555/lunch_boxes/${user.id}`, {
  //     method: "PATCH",
  //     headers: { "Content-Type": "application/json" },
  //     body: JSON.stringify({ snack_id: snack.id }),
  //   }).then((res) =>
  //     res.json().then(() => {
  //       navigate("/lunchbox");
  //     })
  //   );
  // }

  return (
    <div>
      <h4>{prize.name}</h4>
      <p>{`${prize.token_price} Tokens`}</p>
      <img src={prize.image} style={{ width: 200, borderRadius: "20px" }} />
      <button className="bg-yellow-400 hover:bg-yellow-300 rounded-3xl py-2 px-6 shadow-xl transition-all duration-300">
        Get prize
      </button>
    </div>
  );
}

export default Prize;
