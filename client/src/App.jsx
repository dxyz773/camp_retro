// import { useState } from 'react'
import "./App.css";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { campersLoader, drinksLoader } from "./components/apiCampRetro";
import Camp from "./components/Camp";
import CampCabin from "./components/CampCabin";
import Auth from "./components/Auth";
import Snackbar from "./components/SnackBar";
import Drink from "./components/Drink";
import Home from "./components/Home";
import Snacks from "./components/Snacks";
import AppLayout from "./components/AppLayout";

const router = createBrowserRouter([
  {
    element: <AppLayout />,
    children: [
      { path: "/", element: <Home /> },
      { path: "/camp", element: <Camp />, loader: campersLoader },
      { path: "/camp-cabin", element: <CampCabin /> },
      { path: "/auth", element: <Auth /> },
      { path: "/snackbar", element: <Snackbar /> },
      { path: "/snacks", element: <Snacks /> },
      { path: "/drinks", element: <Drink />, loader: drinksLoader },
    ],
  },
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
