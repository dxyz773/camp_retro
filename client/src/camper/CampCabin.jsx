import { useState } from "react";
import Lunchbox from "./Lunchbox";
function CampCabin({ user, api }) {
  const [profile, setProfile] = useState("");
  const { camper_name, username, bio, image, id } = user;

  function addUserInfo() {
    fetch(`${api}/campers/${id}`, {
      method: "PATCH",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ image: profile }),
    });
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
