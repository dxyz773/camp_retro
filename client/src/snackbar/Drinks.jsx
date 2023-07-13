import OneDrink from "./OneDrink";
import Search from "../re-use/Search";
function Drinks({ drinks, search, handleChange }) {
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
