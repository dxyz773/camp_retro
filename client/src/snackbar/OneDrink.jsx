function OneDrink({ drink }) {
  const { image, name, id } = drink;
  return (
    <div>
      <img src={image} alt={name} style={{ width: 200, height: 200 }} />
      <div>
        <h5>{name}</h5>
      </div>
    </div>
  );
}

export default OneDrink;
