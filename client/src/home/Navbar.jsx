import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{ display: "flex", gap: "50px", marginLeft: "20px" }}>
      {" "}
      <NavLink to="/">camp retro</NavLink>
      <NavLink to="/camp">Camp Entrance</NavLink>
      <NavLink to="/camp/cabin">Camp Cabin</NavLink>
      <NavLink to="/camp/drinks">Juice box Stop</NavLink>
      <NavLink to="/camp/snacks">Snack Break</NavLink>
      <NavLink to="/signup">Signup</NavLink>
      <NavLink to="/login">Login</NavLink>
    </nav>
  );
}

export default Navbar;
