import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/">Camp Retro</NavLink>
        </li>
        <li>
          <NavLink to="/auth">Signup | Login</NavLink>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
