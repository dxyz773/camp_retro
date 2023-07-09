function OneSnack({ snack }) {
  return (
    <div>
      <h5>{snack.name}</h5>
      <img src={snack.image} alt={snack.name} style={{ width: 200 }} />
    </div>
  );
}

export default OneSnack;
