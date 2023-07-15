import { NavLink } from "react-router-dom";
function Navbar() {
  return (
    <nav style={{ display: "flex", gap: "50px" }}>
      <NavLink to="/">| camp-Retro |</NavLink>
      <NavLink to="/camp-cabin">Camp Cabin</NavLink>
      <NavLink to="/campers">Meet our campers</NavLink>
      <NavLink to="/campfire">Campfire</NavLink>
      <NavLink to="/snack-break">Snack Break</NavLink>
      <NavLink to="/drink-station">Drink Station</NavLink>
      <NavLink to="/login">Login</NavLink>
    </nav>
  );
}

export default Navbar;
