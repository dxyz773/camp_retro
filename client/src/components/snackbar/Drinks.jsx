import OneDrink from "./OneDrink";
import { useLoaderData } from "react-router-dom";
import { NavLink } from "react-router-dom";
function Drinks() {
  const drinks = useLoaderData();

  return (
    <div>
      <p>Yummy Snacks</p>
      {drinks.map((drink) => (
        <OneDrink key={drink.id} drink={drink} />
      ))}
      <button>
        <NavLink to="/snackbar">Back to Snackbar</NavLink>
      </button>
    </div>
  );
}

export default Drinks;
