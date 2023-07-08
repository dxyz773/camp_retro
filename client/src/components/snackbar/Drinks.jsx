import OneDrink from "./OneDrink";
import { useLoaderData } from "react-router-dom";
import { NavLink } from "react-router-dom";
import Search from "../../ui/Search";
import { useState } from "react";

function Drinks() {
  const drinks = useLoaderData();
  const [search, setSearch] = useState("");

  function handleSearch(e) {
    setSearch(e.target.value);
  }

  let filteredDrinks = drinks.filter((drink) =>
    drink.name.toLowerCase().includes(search.toLowerCase())
  );
  return (
    <div>
      <p>Yummy Snacks</p>
      <Search search={search} onSearch={handleSearch} />
      {filteredDrinks.map((drink) => (
        <OneDrink key={drink.id} drink={drink} />
      ))}
      <button>
        <NavLink to="/snackbar">Back to Snackbar</NavLink>
      </button>
    </div>
  );
}

export default Drinks;
