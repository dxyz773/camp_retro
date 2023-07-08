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
import OneDrink from "./snackbar/OneDrink";
import Snacks from "./snackbar/Snacks";
import OneSnack from "./snackbar/OneSnack";
//----------------------------------------------//
//            OTHER REACT IMPORTS
//----------------------------------------------//
import { Routes, Route } from "react-router-dom";
//----------------------------------------------//
//                    APP
//----------------------------------------------//
function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/camp" element={<Camp />} />
        <Route path="/camp/cabin" element={<CampCabin />} />
        <Route path="/camp/drinks" element={<Drinks />} />
        <Route path="/camp/drinks/:id" element={<OneDrink />} />
        <Route path="/camp/snacks" element={<Snacks />} />
        <Route path="/camp/snacks/:id" element={<OneSnack />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </div>
  );
}

export default App;
