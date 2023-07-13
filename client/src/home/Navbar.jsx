import { NavLink, useNavigate } from "react-router-dom";

function Navbar({ user, token }) {
  const navigate = useNavigate();

  function Logout() {
    fetch("http://127.0.0.1:5555/logout", {
      method: "GET",
      headers: { Authorization: "Bearer " + token },
      credentials: "include",
    }).then((res) => {
      if (res.ok) {
        sessionStorage.removeItem("token");
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
          <p>No token yet</p>
        </div>
      )}
    </nav>
  );
}

export default Navbar;
