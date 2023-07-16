import { NavLink } from "react-router-dom";
import UserContext from "../context/UserContext";
import { useContext } from "react";

function Navbar() {
  const { user } = useContext(UserContext);
  return (
    <nav
      className="bg-yellow-400 text-md py-5"
      style={{ display: "flex", gap: "40px" }}
    >
      <NavLink to="/">| camp-Retro |</NavLink>
      <NavLink to="/camp-cabin">Camp Cabin</NavLink>
      <NavLink to="/campers">Campers</NavLink>
      <NavLink to="/campfire">Campfire</NavLink>
      <NavLink to="/games">GAMES</NavLink>
      <NavLink to="/prize-room">Prize Room</NavLink>
      <NavLink to="/snack-break">Snack Break</NavLink>
      <NavLink to="/drink-station">Drink Station</NavLink>
      <NavLink to="/login">Login</NavLink>
      <p
        style={{ display: "inline-block", marginLeft: "60px" }}
      >{`Welcome, ${user.camper_name}`}</p>
    </nav>
  );
}

export default Navbar;
