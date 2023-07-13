import OneDrink from "./OneDrink";
import Search from "../re-use/Search";
import { useState, useEffect } from "react";
function Drinks({ token }) {
  const [drinks, setDrinks] = useState([]);
  const [search, SetSearch] = useState("");
  function handleChange(e) {
    SetSearch(e.target.value);
  }
  useEffect(() => {
    fetch("http://127.0.0.1:5555/drinks", {
      headers: { Authorization: "Bearer " + token },
    })
      .then((res) => res.json())
      .then((data) => setDrinks(data));
  }, []);
  let searched = drinks.filter((snack) =>
    snack.name.toLowerCase().includes(search.toLowerCase())
  );
  const allDrinks = searched.map((drink) => (
    <OneDrink key={drink.id} drink={drink} />
  ));
  return (
    <div>
      <h3>Take a break and grab a juice box! </h3>
      <Search onSearch={handleChange} search={search} />
      <div>{allDrinks}</div>
    </div>
  );
}

export default Drinks;
