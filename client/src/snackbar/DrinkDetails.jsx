import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
function DrinkDetails() {
  const [drink, setDrink] = useState({});
  const params = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/drinks/${params.id}`).then((res) => {
      if (res.ok) {
        res.json().then((data) => setDrink(data));
      } else {
        navigate("/not-found");
      }
    });
  }, []);

  return (
    <div>
      <h3>{drink.name}</h3>
      <img src={drink.image} alt={drink.name} style={{ width: 400 }} />
    </div>
  );
}

export default DrinkDetails;
