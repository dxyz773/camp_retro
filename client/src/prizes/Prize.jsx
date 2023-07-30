import UserContext from "../context/UserContext";
import { useContext, useState } from "react";

function Prize({ prize }) {
  const { user } = useContext(UserContext);
  const [message, setMessage] = useState("");

  function addPrize() {
    fetch("/api/prizes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: prize.name,
        image: prize.image,
        token_price: prize.token_price,
        treasure_chest_id: user.id,
      }),
    }).then(() => setMessage(`${prize.name} purchased!`));
  }

  return (
    <div
      style={{ width: "200px" }}
      className="hover:scale-105 transition-all duration-200 flex flex-col items-center"
    >
      <div className="px-4">
        <h4>{prize.name}</h4>
        <p className="text-violet-800 font-semibold uppercase tracking-wider">{`${prize.token_price} Tokens`}</p>
      </div>
      <img
        src={prize.image}
        className="shadow-2xl rounded-md shadow-neutral-800"
        style={{
          width: 160,
          borderBottomLeftRadius: 0,
          borderBottomRightRadius: 0,
        }}
      />
      <button
        className="bg-neutral-100 hover:bg-purple-400 rounded-md py-2 shadow-xl text-xs uppercase tracking-widest transition-all duration-300"
        style={{
          borderTopLeftRadius: 0,
          borderTopRightRadius: 0,
          width: "160px",
        }}
        onClick={addPrize}
      >
        {message ? message : `Get ${prize.name}`}
      </button>
    </div>
  );
}

export default Prize;
