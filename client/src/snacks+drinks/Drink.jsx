import { useParams } from "react-router-dom";
function Drink({ drink }) {
  return (
    <div>
      <h4>{drink.name}</h4>
      <img
        src={drink.image}
        style={{ width: 200, borderRadius: "20px" }}
        alt={drink.name}
      />
    </div>
  );
}

export default Drink;
