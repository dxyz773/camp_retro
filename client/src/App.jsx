//----------------------------------------------------------------------------|
//                            COMPONENT IMPORTS
//----------------------------------------------------------------------------|
import Navbar from "./nav/Navbar";
import Home from "./home/Home";
import Login from "./auth/Login";
import Campers from "./campers/Campers";
import CampCabin from "./campers/CampCabin";
import DrinkStation from "./snacks+drinks/DrinkStation";
import SnackBreak from "./snacks+drinks/SnackBreak";
import Campfire from "./campfire/Campfire";
import Snack from "./snacks+drinks/Snack";
import Drink from "./snacks+drinks/Drink";
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
    <>
      <UserContext.Provider value={{ user, updateUser }}>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/campers" element={<Campers />} />
          <Route path="/camp-cabin" element={<CampCabin />} />
          <Route path="/snack-break" element={<SnackBreak />} />
          <Route path="/drink-station" element={<DrinkStation />} />
          <Route path="/campfire" element={<Campfire />} />
        </Routes>
      </UserContext.Provider>
    </>
  );
}

export default App;
