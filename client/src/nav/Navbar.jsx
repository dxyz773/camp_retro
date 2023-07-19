import { NavLink } from "react-router-dom";
import UserContext from "../context/UserContext";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";

function Navbar() {
  const { user } = useContext(UserContext);
  const navigate = useNavigate();
  function handleLogout() {
    fetch("/api/logout").then(navigate("/"));
  }
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

      <p className="ml-5 bg-neutral-100 rounded-xl py-2 pl-5 pr-10">
        Welcome to camp!
      </p>
      <button
        className="hover:text-indigo-600 transition-all duration-200"
        onClick={handleLogout}
      >
        Logout
      </button>
    </nav>
  );
}

export default Navbar;
