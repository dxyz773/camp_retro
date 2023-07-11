import { useEffect, useState } from "react";
import OneSnack from "./OneSnack";
import Search from "../re-use/Search";
function Snacks({}) {
  const [snacks, setSnacks] = useState([]);
  const [search, SetSearch] = useState("");
  function handleChange(e) {
    SetSearch(e.target.value);
  }

  useEffect(() => {
    fetch("http://127.0.0.1:5555/snacks")
      .then((res) => res.json())
      .then((data) => setSnacks(data));
  }, []);

  let searchedSnacks = snacks.filter((snack) =>
    snack.name.toLowerCase().includes(search.toLocaleLowerCase())
  );
  const allSnacks = searchedSnacks.map((snack) => (
    <OneSnack key={snack.id} snack={snack} />
  ));

  return (
    <div>
      <h3>Take a break and grab a juice box! </h3>
      <Search onSearch={handleChange} search={search} />
      <div>{allSnacks}</div>
    </div>
  );
}

export default Snacks;
