import { useState, useEffect } from "react";
function Campers() {
  const [campers, setCampers] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5555/users")
      .then((res) => res.json())
      .then((data) => setCampers(data));
  }, []);
  const allTheCampers = campers.map((camper) => (
    <div style={{ width: 160 }} key={camper.id}>
      <h4>{camper.camp_name}</h4>
      <img
        src={camper.image}
        style={{ width: 100, marginBottom: "5px" }}
        className="rounded-3xl "
      />
      <p
        className="text-xs text-neutral-100"
        style={{ paddingLeft: "40px" }}
      >{`@${camper.camper_name}`}</p>
    </div>
  ));
  return (
    <div
      className="bg-covef bg-[url('https://hearingreview.com/wp-content/uploads/2018/08/dreamstime_m_36706735-1280x640.jpg.webp')]"
      style={{ height: "90vh" }}
    >
      <h3>Campers</h3>

      <div
        // className="rotate-12"
        style={{
          display: "grid",
          transform: "rotate(9deg)",
          gridTemplateColumns: "1fr 1fr 1fr 1fr",
          width: "550px",
          marginLeft: "545px",
          marginTop: "50px",
          rowGap: "20px",
        }}
      >
        {allTheCampers}
      </div>
      <img
        src="https://ih1.redbubble.net/image.1163893532.2610/st,small,507x507-pad,600x600,f8f8f8.jpg"
        width={100}
      />
    </div>
  );
}

export default Campers;
