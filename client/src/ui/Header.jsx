import { Link } from "react-router-dom";
function Header() {
  return (
    <header style={{ display: "flex", justifyContent: "space-evenly" }}>
      <Link to="/">camp retro logo</Link>
      <Link to="/camp">Camp Entrance</Link>
      <Link to="/camp-cabin">Camp Cabin</Link>
      <Link to="/snackbar">Snackbar</Link>
      <Link to="/auth">Login | Signup</Link>
      <p>Welcome, user</p>
    </header>
  );
}

export default Header;
