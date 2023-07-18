//----------------------------------------------------------------------------|
//                            COMPONENT IMPORTS
//----------------------------------------------------------------------------|
import Navbar from "./nav/Navbar";
import Home from "./home/Home";
import Login from "./auth/Login";
import Signup from "./auth/Signup";
import Campers from "./campers/Campers";
import CampCabin from "./campers/CampCabin";
import DrinkStation from "./snacks+drinks/DrinkStation";
import SnackBreak from "./snacks+drinks/SnackBreak";
import Campfire from "./campfire/Campfire";
import LunchBox from "./campers/LunchBox";
import TreasureChest from "./campers/TreasureChest";
import PrizeRoom from "./prizes/PrizeRoom";
import Games from "./games/Games";
import RPC from "./games/RPC";

//----------------------------------------------------------------------------|
//                            OTHER IMPORTS
//----------------------------------------------------------------------------|

import { useState, useEffect } from "react";
import { Route, Routes } from "react-router-dom";
import UserContext from "./context/UserContext";

function App() {
  const [user, setUser] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:5555/check_session")
      .then((res) => res.json())
      .then((data) => {
        setUser(data);
        console.log(data);
      });
  }, []);

  function updateUser(data) {
    setUser(data);
  }
  return (
    <div>
      <UserContext.Provider value={{ user, updateUser }}>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/campers" element={<Campers />} />
          <Route path="/camp-cabin" element={<CampCabin />} />
          <Route path="/lunchbox" element={<LunchBox />} />
          <Route path="/treasure-chest" element={<TreasureChest />} />
          <Route path="/snack-break" element={<SnackBreak />} />
          <Route path="/drink-station" element={<DrinkStation />} />
          <Route path="/games" element={<Games />} />
          <Route path="/prize-room" element={<PrizeRoom />} />
          <Route path="/campfire" element={<Campfire />} />
          <Route path="/rock-paper-scissors" element={<RPC />} />
        </Routes>
      </UserContext.Provider>
    </div>
  );
}

export default App;
