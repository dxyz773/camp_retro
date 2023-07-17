import { useState, useEffect } from "react";
function Campers() {
  const [campers, setCampers] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5555/users")
      .then((res) => res.json())
      .then((data) => setCampers(data));
  }, []);
  const allTheCampers = campers.map((camper) => (
    <div
      style={{
        width: 135,
        display: "flex",
        flexDirection: "column",
        backgroundColor: "white",
        alignItems: "center",
        borderRadius: "2px",
      }}
      key={camper.id}
    >
      <h4>{camper.camp_name}</h4>

      <img
        src={camper.image}
        style={{ width: 100, marginBottom: "5px", marginTop: "10px" }}
        className="rounded-sm shadow-md shadow-neutral-800 hover:scale-105 transition-all duration-300"
      />
      <p
        className="text-xs text-neutral-900"
        style={{ paddingLeft: "40px" }}
      >{`@${camper.username}`}</p>
    </div>
  ));
  return (
    <div style={{ position: "relative" }}>
      <div
        className="bg-covef bg-[url('https://hearingreview.com/wp-content/uploads/2018/08/dreamstime_m_36706735-1280x640.jpg.webp')]"
        style={{ height: "85vh" }}
      >
        <h3
          style={{
            position: "absolute",
            top: 80,
            left: 265,
            transform: "rotate(-16deg)",
          }}
          className="text-5xl tracking-tight text-neutral-900 font-extrabold uppercase drop-shadow-md"
        >
          Campers
        </h3>

        <div
          style={{
            display: "grid",
            transform: "rotate(9.7deg)",
            gridTemplateColumns: "1fr 1fr 1fr 1fr",
            width: "550px",
            rowGap: "15px",
            position: "absolute",
            columnGap: "12px",
            top: 55,
            right: 315,
          }}
        >
          {allTheCampers}
        </div>
        <img
          className="shadow-md shadow-neutral-800"
          src="https://cdn.vectorstock.com/i/preview-2x/84/65/groovy-retro-flowers-daisy-hippie-psychedelic-vector-42788465.webp"
          style={{
            position: "absolute",
            top: 360,
            left: 420,
            width: 100,
            borderRadius: "100%",
          }}
        />
        <img
          className="shadow-md shadow-neutral-800"
          src="https://ih1.redbubble.net/image.1163893532.2610/st,small,507x507-pad,600x600,f8f8f8.jpg"
          style={{
            position: "absolute",
            top: 25,
            right: 205,
            width: 80,
            transform: "rotate(-16deg)",
            borderRadius: "100%",
          }}
        />
      </div>
    </div>
  );
}

export default Campers;
