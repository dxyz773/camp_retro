import { useState, useEffect } from "react";
function Campers() {
  const [campers, setCampers] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5555/users")
      .then((res) => res.json())
      .then((data) => setCampers(data));
  }, []);
  const allTheCampers = campers.map((camper) => (
    <div key={camper.id}>
      <h4>{camper.camp_name}</h4>
      <img src={camper.image} style={{ width: 200, borderRadius: "30px" }} />
      <p>{camper.bio}</p>
    </div>
  ));
  return (
    <div>
      <h3>Campers</h3>

      {allTheCampers}
    </div>
  );
}

export default Campers;
