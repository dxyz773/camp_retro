function OneSnack({ snack }) {
  return (
    <div>
      <p>{snack.name}</p>
      <img
        src={snack.image}
        alt={snack.name}
        style={{ width: 200, borderRadius: "20px" }}
      />
    </div>
  );
}

export default OneSnack;
