import OneSnack from "./OneSnack";
import Search from "../re-use/Search";
function Snacks({ snacks, search, handleChange }) {
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
