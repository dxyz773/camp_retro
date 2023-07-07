import { NavLink } from "react-router-dom";
function Snackbar() {
  return (
    <div>
      <p>Snackbar </p>
      <ul style={{ listStyle: "none" }}>
        <li>
          <NavLink to="/drinks">Drinks</NavLink>
        </li>
        <li>
          <NavLink to="/snacks">Snacks</NavLink>
        </li>
      </ul>
    </div>
  );
}

export default Snackbar;
