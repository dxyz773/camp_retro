//----------------------------------------------//
//             COMPONENT IMPORTS
//----------------------------------------------//
import Navbar from "./home/Navbar";
import Home from "./home/Home";
import Login from "./auth/Login";
import Signup from "./auth/Signup";
import Camp from "./camper/Camp";
import CampCabin from "./camper/CampCabin";
import Drinks from "./snackbar/Drinks";
import DrinkDetails from "./snackbar/DrinkDetails";
import Snacks from "./snackbar/Snacks";
import SnackDetails from "./snackbar/SnackDetails";
//----------------------------------------------//
//            OTHER REACT IMPORTS
//----------------------------------------------//
import { Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
//----------------------------------------------//
//                    APP
//----------------------------------------------//
const api = "http://127.0.0.1:5555";
function App() {
  const [user, setUser] = useState(null);
  useEffect(() => {
    getUser();
  }, []);

  function updateUser(user) {
    setUser(user);
  }
  function getUser() {
    fetch(`${api}/authorized-session`).then((res) => {
      if (res.ok) {
        res.json().then((data) => setUser(data));
      } else {
        setUser(null);
      }
    });
  }
  if (!user) {
    return (
      <div>
        <Navbar updateUser={updateUser} user={user} api={api} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/login"
            element={<Login api={api} updateUser={updateUser} />}
          />
          <Route
            path="/signup"
            element={<Signup api={api} updateUser={updateUser} />}
          />
        </Routes>
      </div>
    );
  }
  return (
    <div>
      <Navbar updateUser={updateUser} user={user} api={api} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/camp" element={<Camp api={api} />} />
        <Route
          path="/camp/cabin"
          element={<CampCabin user={user} api={api} />}
        />
        <Route path="/camp/drinks" element={<Drinks api={api} />} />
        <Route path="/camp/drinks/:id" element={<DrinkDetails />} />
        <Route path="/camp/snacks" element={<Snacks api={api} />} />
        <Route path="/camp/snacks/:id" element={<SnackDetails />} />
        <Route path="/login" element={<Login api={api} />} />
        <Route path="/signup" element={<Signup api={api} />} />
      </Routes>
    </div>
  );
}

export default App;
