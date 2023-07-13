function OneSnack({ snack }) {
  const { image, name, id } = snack;
  return (
    <div>
      <img src={image} alt={name} style={{ width: 200 }} />
      <div>
        <h5>{name}</h5>
      </div>
    </div>
  );
}

export default OneSnack;
