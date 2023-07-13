import { NavLink, useNavigate } from "react-router-dom";

function Navbar({ user, updateUser }) {
  const navigate = useNavigate();

  function Logout() {
    fetch("http://127.0.0.1:5555/logout", {
      method: "GET",
      credentials: "include",
    }).then((res) => {
      if (res.ok) {
        updateUser(null);
        navigate("/");
      }
    });
  }
  return (
    <nav>
      {user ? (
        <div style={{ display: "flex", gap: "50px", marginLeft: "20px" }}>
          <NavLink to="/">camp retro</NavLink>
          <NavLink to="/camp">Camp Entrance</NavLink>
          <NavLink to="/camp/cabin">Camp Cabin</NavLink>
          <NavLink to="/camp/drinks">Juice box Stop</NavLink>
          <NavLink to="/camp/snacks">Snack Break</NavLink>
          <NavLink to="/camp/lunchbox">Lunchbox</NavLink>
          <button onClick={Logout}>Log Out</button>
          <p style={{ marginTop: "8px" }}>{`Welcome: ${user.username}`}</p>
        </div>
      ) : (
        <div style={{ display: "flex", gap: "50px", marginLeft: "20px" }}>
          <NavLink to="/">camp retro</NavLink>
          <NavLink to="/signup">Signup</NavLink>
          <NavLink to="/login">Login</NavLink>
        </div>
      )}
    </nav>
  );
}

export default Navbar;
