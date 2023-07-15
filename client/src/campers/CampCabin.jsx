import UserContext from "../context/UserContext";
import { useContext } from "react";
import { NavLink } from "react-router-dom";

function CampCabin() {
  const { user } = useContext(UserContext);

  return (
    <div>
      <h2>Camp Cabin</h2>
      <h4>Welcome to your camp cabin, {user.camper_name}</h4>
      <img
        src={user.image}
        alt={user.username}
        style={{ width: 200, borderRadius: "30px" }}
      />
      <div>
        <p>Bio:{user.bio}</p>
      </div>
      <div>
        <img src={user.lunch_box[0].image} alt="lunchbox" width={200} />
        <button>
          <NavLink to="/lunchbox">Lunchbox</NavLink>
        </button>
        <br />
        <button>
          <NavLink to="/treasure-chest">Treasure Chest</NavLink>
        </button>
      </div>
    </div>
  );
}

export default CampCabin;
