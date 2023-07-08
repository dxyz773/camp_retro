import { RouterProvider, createBrowserRouter } from "react-router-dom";
import {
  campersLoader,
  drinksLoader,
  snacksLoader,
} from "./services/apiCampRetro";
import Camp from "./components/campers/Camp";
import CampCabin from "./components/campers/CampCabin";
import Auth from "./components/auth/Auth";
import Snackbar from "./components/snackbar/SnackBar";
import Drinks from "./components/snackbar/Drinks";
import Home from "./components/home/Home";
import Snacks from "./components/snackbar/Snacks";
import OneSnack from "./components/snackbar/OneSnack";
import OneDrink from "./components/snackbar/OneDrink";
import Error from "./ui/Error";
import AppLayout from "./ui/AppLayout";

const router = createBrowserRouter([
  {
    element: <AppLayout />,
    errorElement: <Error />,
    children: [
      { path: "/", element: <Home /> },
      { path: "/camp", element: <Camp />, loader: campersLoader },
      { path: "/camp-cabin", element: <CampCabin /> },
      { path: "/auth", element: <Auth /> },
      { path: "/snackbar", element: <Snackbar /> },
      { path: "/snacks", element: <Snacks />, loader: snacksLoader },
      { path: "/drinks", element: <Drinks />, loader: drinksLoader },
      { path: "/drinks/one", element: <OneDrink /> },
      { path: "/snacks/one", element: <OneSnack /> },
    ],
  },
]);
function App() {
  return <RouterProvider router={router} />;
}

export default App;
