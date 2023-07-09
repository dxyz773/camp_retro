import { Link } from "react-router-dom";
function OneDrink({ drink }) {
  const { image, name, id } = drink;
  return (
    <div>
      <img src={image} alt={name} style={{ width: 200 }} />
      <div>
        <Link to={`/camp/drinks/${id}`}>
          <h5>{name}</h5>
        </Link>
      </div>
    </div>
  );
}

export default OneDrink;
