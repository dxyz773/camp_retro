import UserContext from "../context/UserContext";
import { useContext } from "react";
import { NavLink } from "react-router-dom";

function CampCabin() {
  const { user } = useContext(UserContext);

  return (
    <div
      className="bg-cover bg-[url('https://images.unsplash.com/photo-1622066737704-c5d990e137fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2670&q=80')]"
      style={{ height: "100vh" }}
    >
      <h2>Camp Cabin</h2>
      <h4 style={{ paddingTop: "50px" }}>
        Welcome to your camp cabin, {user.camper_name}
      </h4>
      <img
        src={user.image}
        alt={user.username}
        style={{ width: 200, borderRadius: "30px" }}
      />
      <div>
        <p>Bio:{user.bio}</p>
      </div>
      <div className="w-fit">
        <NavLink to="/lunchbox">
          <img
            src={user.lunch_box[0].image}
            alt="lunchbox"
            width={200}
            className="rounded-2xl"
          />
        </NavLink>
        <NavLink to="/treasure-chest">
          <img
            src={user.treasure_chest[0].image}
            alt="lunchbox"
            width={200}
            className="rounded-2xl"
          />
        </NavLink>
      </div>
    </div>
  );
}

export default CampCabin;
