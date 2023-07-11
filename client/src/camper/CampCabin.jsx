import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Lunchbox from "./Lunchbox";
function CampCabin({ user }) {
  const [profile, setProfile] = useState("");
  const { camper_name, username, bio, image, id } = user;

  function addUserInfo() {
    const navigate = useNavigate();
    fetch(`http://127.0.0.1:5555/campers/${id}`, {
      method: "PATCH",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ image: profile }),
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
      <div>
        <h3>Lunchbox</h3>
        <Lunchbox user={user} />
      </div>
    </div>
  );
}

export default CampCabin;
