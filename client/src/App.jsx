//----------------------------------------------//
//             COMPONENT IMPORTS
//----------------------------------------------//
import Navbar from "./home/Navbar";
import Home from "./home/Home";
import Login from "./auth/Login";
import Signup from "./auth/Signup";
import Camp from "./camper/Camp";
import CampCabin from "./camper/CampCabin";
import Lunchbox from "./camper/Lunchbox";
import Drinks from "./snackbar/Drinks";
import Snacks from "./snackbar/Snacks";

//----------------------------------------------//
//            OTHER REACT IMPORTS
//----------------------------------------------//
import { Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";

//----------------------------------------------//
//                    APP
//----------------------------------------------//

function App() {
  const [user, setUser] = useState(null);
  const [campers, setCampers] = useState([]);
  const [snacks, setSnacks] = useState([]);
  const [drinks, setDrinks] = useState([]);
  const [search, SetSearch] = useState("");

  useEffect(() => {
    getUser();
    getSnacks();
    getDrinks();
    getCampers();
  }, []);

  // ---------------------------------------------------------------------------|
  //                              USER
  // ---------------------------------------------------------------------------|

  const getUser = () =>
    fetch("http://127.0.0.1:5555/check_session").then((res) => {
      if (res.ok) {
        res.json().then((data) => {
          setUser(data);
        });
      } else {
        setUser(null);
      }
    });

  function updateUser(user) {
    setUser(user);
  }

  // ---------------------------------------------------------------------------|
  //                                CAMPERS
  // ---------------------------------------------------------------------------|

  function getCampers() {
    fetch("http://127.0.0.1:5555/users")
      .then((res) => res.json())
      .then((data) => setCampers(data));
  }
  // ---------------------------------------------------------------------------|
  //                             SNACKS
  // --------------------------------------------------------------------------|
  function getSnacks() {
    fetch("http://127.0.0.1:5555/snacks")
      .then((res) => res.json())
      .then((data) => setSnacks(data));
  }

  function getDrinks() {
    fetch("http://127.0.0.1:5555/drinks")
      .then((res) => res.json())
      .then((data) => setDrinks(data));
  }
  // ---------------------------------------------------------------------------|
  //                           REUSABLE FUNCTIONS
  // --------------------------------------------------------------------------|
  function handleChange(e) {
    SetSearch(e.target.value);
  }

  return (
    <div>
      <Navbar updateUser={updateUser} user={user} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/camp" element={<Camp campers={campers} />} />
        <Route
          path="/camp/cabin"
          element={<CampCabin user={user} updateUser={updateUser} />}
        />
        <Route path="/camp/lunchbox" element={<Lunchbox />} />
        <Route
          path="/camp/drinks"
          element={
            <Drinks
              drinks={drinks}
              search={search}
              handleChange={handleChange}
            />
          }
        />
        <Route
          path="/camp/snacks"
          element={
            <Snacks
              snacks={snacks}
              search={search}
              handleChange={handleChange}
            />
          }
        />

        <Route path="/login" element={<Login updateUser={updateUser} />} />
        <Route path="/signup" element={<Signup updateUser={updateUser} />} />
      </Routes>
    </div>
  );
}

export default App;
