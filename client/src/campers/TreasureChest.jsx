import UserContext from "../context/UserContext";
import { useContext, useEffect } from "react";

function TreasureChest() {
  const { user, updateUser } = useContext(UserContext);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/check_session")
      .then((res) => res.json())
      .then((data) => updateUser(data));
  }, []);

  const allTreasure = user.treasure_chest[0].prizes.map((prize) => (
    <div key={prize.id} className="flex flex-col">
      <div className="rounded-2xl px-4 bg-white mb-2 bg-opacity-80">
        <p className="text-xl font-semibold mb-3">{prize.name}</p>
      </div>
      <img
        src={prize.image}
        alt={prize.name}
        width={200}
        className="shadow-xl rounded-3xl hover:scale-105 shadow-neutral-800 transition-all duration-300"
      />
    </div>
  ));
  return (
    <div
      className="bg-cover bg-[url('https://images.unsplash.com/photo-1516462919870-8bcf749b0135?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80')]"
      style={{ height: "100vh", display: "flex", justifyContent: "flex-end" }}
    >
      <div className="flex flex-col p-12 bg-pink-500 rounded-dm bg-opacity-50 w-6/12">
        <div className="text-4xl ml-48 mb-10 font-semibold">
          <h3 className="tracking-wide">Treasure Chest</h3>
        </div>
        <section className="flex gap-20 ml-10">{allTreasure}</section>
      </div>
    </div>
  );
}

export default TreasureChest;
