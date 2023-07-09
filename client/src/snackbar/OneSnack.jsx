import { Link } from "react-router-dom";
function OneSnack({ snack }) {
  const { image, name, id } = snack;
  return (
    <div>
      <img src={image} alt={name} style={{ width: 200 }} />
      <div>
        <Link to={`/camp/snacks/${id}`}>
          <h5>{name}</h5>
        </Link>
      </div>
    </div>
  );
}

export default OneSnack;
