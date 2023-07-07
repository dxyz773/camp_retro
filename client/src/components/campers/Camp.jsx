import { useLoaderData } from "react-router-dom";
function Camp() {
  const campers = useLoaderData();
  const allCampers = campers.map((camper) => (
    <div key={camper.id} style={{ display: "inline-block" }}>
      <p>{camper.camper_name}</p>
      <img
        src={camper.image}
        alt={camper.camper_name}
        width="100"
        style={{ borderRadius: "20px", marginLeft: "10px" }}
      />
      <p>{camper.bio}</p>
    </div>
  ));
  return (
    <div>
      <h3>Welcome to camp!</h3>
      {allCampers}
    </div>
  );
}

export default Camp;
