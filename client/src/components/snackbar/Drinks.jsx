import { useLoaderData } from "react-router-dom";
function Drinks() {
  const drinks = useLoaderData();
  const allDrinks = drinks.map((drink) => (
    <div key={drink.id} style={{ display: "inline-block" }}>
      <p>{drink.name}</p>
      <img
        src={drink.image}
        alt={drink.name}
        width="200"
        style={{ borderRadius: "100%" }}
      />
    </div>
  ));
  return (
    <div>
      <p>Yummy Snacks</p>
      {allDrinks}
    </div>
  );
}

export default Drinks;
