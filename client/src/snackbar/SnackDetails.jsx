import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
function SnackDetails() {
  const [snack, setSnack] = useState({});
  const params = useParams();
  const navigate = useNavigate();
  useEffect(() => {
    fetch(`http://127.0.0.1:5555/snacks/${params.id}`).then((res) => {
      if (res.ok) {
        res.json().then((data) => setSnack(data));
      } else {
        navigate("/not-found");
      }
    });
  }, []);
  return (
    <div>
      <h3>{snack.name}</h3>
      <img src={snack.image} alt={snack.name} style={{ width: 600 }} />
    </div>
  );
}

export default SnackDetails;
