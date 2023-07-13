import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { NavLink } from "react-router-dom";
function CampCabin({ user, token, updateUser }) {
  const [profile, setProfile] = useState("");
  const { camper_name, username, bio, image, id } = user;

  const navigate = useNavigate();

  function addUserInfo() {
    fetch(`http://127.0.0.1:5555/users/${id}`, {
      method: "PATCH",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({ image: profile }),
    }).then(navigate("/"));
  }

  function handleGetLunchbox() {
    fetch("http://127.0.0.1:5555/lunch_boxes", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: id }),
    }).then(navigate("/"));
  }
  return (
    <div>
      <h3>Camper Name: {camper_name}</h3>
      <img src={image} alt={camper_name} style={{ width: 300 }} />
      <h5>Username: {username}</h5>
      <p>Bio:{bio}</p>
      <div>
        <form onSubmit={addUserInfo}>
          <label htmlFor="add">Add Image:</label>
          <input
            type="text"
            id="add"
            name="add"
            value={profile}
            onChange={(e) => setProfile(e.target.value)}
          />
          <input type="submit" />
        </form>
      </div>
      <div style={{ display: "flex", gap: "20px" }}>
        <button>
          <NavLink to="/camp/lunchbox">Check your snack and drinks</NavLink>
        </button>
        <button onClick={handleGetLunchbox}>Get Lunchbox</button>
      </div>
    </div>
  );
}

export default CampCabin;
