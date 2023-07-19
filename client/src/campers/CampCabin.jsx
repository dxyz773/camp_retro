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
      <div className="pt-8 pl-14 bg-amber-900 bg-opacity-40 pb-44">
        <div className="bg-neutral-100 pl-5 bg-opacity-80 py-6 rounded-md w-fit pr-5">
          <h4 className="text-2xl font-bold pb-6">
            Welcome to your camp cabin, {user.camper_name}
          </h4>
          <img
            src={user.image}
            alt={user.username}
            className="rounded-md shadow-neutral-900 shadow-md"
            style={{ width: 200 }}
          />
          <div>
            <p className="w-60 my-6">Bio: {user.bio}</p>
          </div>
          <div className="w-fit flex items-center gap-8">
            <NavLink to="/lunchbox">
              <img
                src={user.lunch_box[0].image}
                alt="lunchbox"
                width={200}
                className="rounded-md shadow-neutral-700 shadow-md hover:scale-105 transition-all duration-300"
              />
            </NavLink>
            <NavLink to="/treasure-chest">
              <img
                src={user.treasure_chest[0].image}
                alt="lunchbox"
                width={200}
                className="rounded-md shadow-neutral-700 shadow-md hover:scale-105 transition-all duration-300"
              />
            </NavLink>
          </div>
        </div>
      </div>
    </div>
  );
}

export default CampCabin;
