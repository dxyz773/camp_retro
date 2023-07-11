import { useEffect, useState } from "react";
function Camp() {
  const [camper, setCamper] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5555/campers")
      .then((res) => res.json())
      .then((data) => setCamper(data));
  }, []);

  const campers = camper.map((camp) => (
    <img
      key={camp.id}
      src={camp.image}
      style={{ width: 200, borderRadius: "30px" }}
    />
  ));
  return (
    <div>
      <h3>Camp retro entrance</h3>
      {campers}
    </div>
  );
}

export default Camp;
