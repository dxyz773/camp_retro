import { useLoaderData } from "react-router-dom";
function Drink() {
  const drinks = useLoaderData();
  console.log(drinks);
  return <div>Yummy Drinks</div>;
}

export default Drink;
