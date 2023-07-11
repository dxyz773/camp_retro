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
import DrinkDetails from "./snackbar/DrinkDetails";
import Snacks from "./snackbar/Snacks";
import SnackDetails from "./snackbar/SnackDetails";
//----------------------------------------------//
//            OTHER REACT IMPORTS
//----------------------------------------------//
import { Routes, Route } from "react-router-dom";
import { useState } from "react";
// import { useEffect, useState } from "react";
//----------------------------------------------//
//                    APP
//----------------------------------------------//
// const api = "http://127.0.0.1:5555";

function App() {
  const [user, setUser] = useState(null);

  // useEffect(() => {
  //   if (user == null) {
  //     fetch("http://127.0.0.1:5555/check_session")
  //       .then((res) => {
  //         if (res.ok) {
  //           res.json().then((data) => {
  //             setUser(data);
  //           });
  //         }
  //       })
  //       .catch((error) => {
  //         console.log(error);
  //       });
  //   }
  // }, []);

  function updateUser(user) {
    setUser(user);
  }

  if (!user) {
    return (
      <>
        <Navbar updateUser={updateUser} user={user} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login updateUser={updateUser} />} />
          <Route path="/signup" element={<Signup updateUser={updateUser} />} />
        </Routes>
      </>
    );
  }
  return (
    <div>
      <Navbar updateUser={updateUser} user={user} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/camp" element={<Camp />} />
        <Route path="/camp/cabin" element={<CampCabin user={user} />} />
        <Route path="camp/lunchbox" element={<Lunchbox />} />
        <Route path="/camp/drinks" element={<Drinks user={user} />} />
        <Route path="/camp/drinks/:id" element={<DrinkDetails />} />
        <Route path="/camp/snacks" element={<Snacks user={user} />} />
        <Route path="/camp/snacks/:id" element={<SnackDetails />} />
        <Route path="/login" element={<Login updateUser={updateUser} />} />
        <Route path="/signup" element={<Signup updateUser={updateUser} />} />
      </Routes>
    </div>
  );
}

export default App;
