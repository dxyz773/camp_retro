function Snack({ snack }) {
  return (
    <div>
      <h4>{snack.name}</h4>
      <img src={snack.image} style={{ width: 200, borderRadius: "20px" }} />
    </div>
  );
}

export default Snack;
