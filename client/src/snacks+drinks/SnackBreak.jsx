import { useState, useEffect } from "react";
import Search from "../reusable/Search";
import Snack from "./Snack";

function SnackBreak() {
  const [snacks, setSnacks] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5555/snacks")
      .then((res) => res.json())
      .then((data) => setSnacks(data));
  }, []);

  function handleChange(e) {
    setSearch(e.target.value);
  }

  let searchedSnacks = snacks.filter((snack) =>
    snack.name.toLowerCase().includes(search.toLowerCase())
  );
  const allSnacks = searchedSnacks.map((snack) => (
    <Snack key={snack.id} snack={snack} />
  ));
  return (
    <div className="bg-amber-50 px-5" style={{ height: "150vh" }}>
      <p className="text-4xl font-semibold pt-5">Take a snack break 🍎</p>
      <Search handleChange={handleChange} search={search} />
      <div
        className="grid grid-cols-6 gap-y-5
       py-10"
      >
        {allSnacks}
      </div>
    </div>
    //
  );
}

export default SnackBreak;
