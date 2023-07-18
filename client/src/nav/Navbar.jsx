import { NavLink } from "react-router-dom";
import UserContext from "../context/UserContext";
import { useContext } from "react";

function Navbar() {
  const { user } = useContext(UserContext);
  return (
    <nav className="bg-yellow-400 text-md py-5 flex gap-7 items-center">
      <NavLink className="ml-2" to="/">
        <img
          src="https://static.vecteezy.com/system/resources/previews/013/666/396/original/groovy-retro-flower-png.png"
          className="w-14 shadow-md rounded-full bg-yellow-300 hover:rotate-6 transition-all duration-100"
        />
      </NavLink>
      <NavLink
        className="hover:text-indigo-600 transition-all duration-200"
        to="/camp-cabin"
      >
        Camp Cabin
      </NavLink>
      <NavLink
        className="hover:text-indigo-600 transition-all duration-200"
        to="/campers"
      >
        Campers
      </NavLink>
      <NavLink
        className="hover:text-indigo-600 transition-all duration-200"
        to="/campfire"
      >
        Campfire
      </NavLink>
      <NavLink
        className="hover:text-indigo-600 transition-all duration-200"
        to="/games"
      >
        GAMES
      </NavLink>
      <NavLink
        className="hover:text-indigo-600 transition-all duration-200"
        to="/prize-room"
      >
        Prize Room
      </NavLink>
      <NavLink
        className="hover:text-indigo-600 transition-all duration-200"
        to="/snack-break"
      >
        Snack Break
      </NavLink>
      <NavLink
        className="hover:text-indigo-600 transition-all duration-200"
        to="/drink-station"
      >
        Drink Station
      </NavLink>
      <div>
        <NavLink
          className="hover:text-indigo-600 transition-all duration-200"
          to="/login"
        >
          Login |
        </NavLink>
        <NavLink
          className="hover:text-indigo-600 transition-all duration-200"
          to="/signup"
        >
          Signup
        </NavLink>
      </div>
      <p className="ml-5 bg-neutral-100 rounded-xl py-2 pr-20 px-3">{`Welcome, ${user.camper_name}`}</p>
    </nav>
  );
}

export default Navbar;
