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
  //

  return (
    <div className="bg-amber-50 px-5" style={{ height: "150vh" }}>
      <p className="text-4xl font-semibold pt-5">
        Stay hydrated! Grab a drink 🥤
      </p>
      <Search handleChange={handleChange} search={search} />
      <div className="grid grid-cols-6 gap-y-2 py-10">{allDrinks}</div>
    </div>
  );
}

export default DrinkStation;
