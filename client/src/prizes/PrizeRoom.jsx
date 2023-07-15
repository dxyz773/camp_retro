import Search from "../reusable/Search";
import Prize from "./Prize";
import { useEffect, useState } from "react";
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
    <div>
      <p>Find your favorite prizes! </p>
      <Search handleChange={handleChange} search={search} />
      {allPrizes}
    </div>
  );
}

export default PrizeRoom;
