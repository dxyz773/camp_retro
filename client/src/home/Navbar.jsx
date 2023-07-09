import { NavLink, useNavigate } from "react-router-dom";

function Navbar({ updateUser, user, api }) {
  const navigate = useNavigate();

  function Logout() {
    fetch(`${api}/logout`).then((res) => {
      if (res.ok) {
        updateUser(null);
        navigate("/");
      }
    });
  }
  return (
    <nav style={{ display: "flex", gap: "50px", marginLeft: "20px" }}>
      <NavLink to="/">camp retro</NavLink>
      <NavLink to="/camp">Camp Entrance</NavLink>
      <NavLink to="/camp/cabin">Camp Cabin</NavLink>
      <NavLink to="/camp/drinks">Juice box Stop</NavLink>
      <NavLink to="/camp/snacks">Snack Break</NavLink>
      <NavLink to="/signup">Signup</NavLink>
      <NavLink to="/login">Login</NavLink>
      {user ? (
        <div>
          <button onClick={Logout}>Log Out</button>
          <p style={{ marginTop: "8px" }}>Hello, {user.username}</p>
        </div>
      ) : (
        ""
      )}
    </nav>
  );
}

export default Navbar;
