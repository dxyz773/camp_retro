import { useEffect, useState } from "react";
import Search from "../reusable/Search";
import Prize from "./Prize";

function PrizeRoom() {
  const [prizes, setPrizes] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5555/prizes")
      .then((res) => res.json())
      .then((data) => setPrizes(data));
  }, []);

  function handleChange(e) {
    setSearch(e.target.value);
  }
  let searchedPrizes = prizes.filter((prize) =>
    prize.name.toLowerCase().includes(search.toLowerCase())
  );
  const allPrizes = searchedPrizes.map((prize) => (
    <Prize key={prize.id} prize={prize} />
  ));

  return (
    <div
      className="bg-cover bg-[url('https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80')] px-5"
      style={{ height: "200vh" }}
    >
      <p className="text-4xl font-semibold pt-5">Prize Room </p>
      <Search handleChange={handleChange} search={search} />
      <div
        className="grid grid-cols-6 gap-y-5
       py-10 bg-pink-500 mb-2 mt-6 bg-opacity-50 rounded-sm"
      >
        {allPrizes}
      </div>
    </div>
  );
}

export default PrizeRoom;
