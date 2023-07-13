function Camp({ campers }) {
  const allTheCampers = campers.map((camper) => (
    <img
      key={camper.id}
      src={camper.image}
      style={{ width: 200, borderRadius: "30px" }}
    />
  ));
  return (
    <div>
      <h3>Camp retro entrance</h3>
      {allTheCampers}
    </div>
  );
}

export default Camp;
