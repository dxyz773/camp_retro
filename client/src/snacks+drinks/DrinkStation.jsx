import Search from "../reusable/Search";
import Drink from "./Drink";
import { useEffect, useState } from "react";
function DrinkStation() {
  const [drinks, setDrinks] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5555/drinks")
      .then((res) => res.json())
      .then((data) => setDrinks(data));
  }, []);

  function handleChange(e) {
    setSearch(e.target.value);
  }
  let searchedDrinks = drinks.filter((drink) =>
    drink.name.toLowerCase().includes(search.toLowerCase())
  );
  const allDrinks = searchedDrinks.map((drink) => (
    <Drink key={drink.id} drink={drink} />
  ));

  return (
    <div>
      <p>Find your favorites </p>
      <Search handleChange={handleChange} search={search} />
      {allDrinks}
    </div>
  );
}

export default DrinkStation;
