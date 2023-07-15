import UserContext from "../context/UserContext";
import { useContext } from "react";
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
      <p>Bio:{user.bio}</p>
    </div>
  );
}

export default CampCabin;
