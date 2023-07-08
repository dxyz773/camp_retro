import { useLoaderData } from "react-router-dom";
import { useState } from "react";
import OneSnack from "./OneSnack";
import { NavLink } from "react-router-dom";
import Search from "../../ui/Search";
function Snacks() {
  const snacks = useLoaderData();
  const [search, setSearch] = useState("");
  function handleSearch(e) {
    setSearch(e.target.value);
  }

  let filteredSnacks = snacks.filter((snack) =>
    snack.name.toLowerCase().includes(search.toLowerCase())
  );
  return (
    <div>
      <p>Yummy Snacks</p>
      <Search onSearch={handleSearch} search={search} />
      {filteredSnacks.map((snack) => (
        <OneSnack key={snack.id} snack={snack} />
      ))}
      <button>
        <NavLink to="/snackbar">Back to Snackbar</NavLink>
      </button>
    </div>
  );
}

export default Snacks;
