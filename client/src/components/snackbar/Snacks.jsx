import { useLoaderData } from "react-router-dom";
import OneSnack from "./OneSnack";
import { NavLink } from "react-router-dom";
function Snacks() {
  const snacks = useLoaderData();

  return (
    <div>
      <p>Yummy Snacks</p>
      {snacks.map((snack) => (
        <OneSnack key={snack.id} snack={snack} />
      ))}
      <button>
        <NavLink to="/snackbar">Back to Snackbar</NavLink>
      </button>
    </div>
  );
}

export default Snacks;
