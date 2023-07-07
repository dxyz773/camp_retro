// import { useState } from 'react'
import "./App.css";
// import Navbar from "./components/Navbar";

import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { camperLoader } from "./components/apiCampRetro";
import Camp from "./components/Camp";
import CampCabin from "./components/CampCabin";
import Auth from "./components/Auth";
import Snackbar from "./components/SnackBar";
import Drink from "./components/Drink";
import Home from "./components/Home";
import AppLayout from "./components/AppLayout";

const router = createBrowserRouter([
  {
    element: <AppLayout />,
    children: [
      { path: "/", element: <Home /> },
      { path: "/camp", element: <Camp /> },
      { path: "/camp-cabin", element: <CampCabin />, loader: camperLoader },
      { path: "/auth", element: <Auth /> },
      { path: "/snackbar", element: <Snackbar /> },
      { path: "/drink/:id", element: <Drink /> },
    ],
  },
]);
function App() {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
