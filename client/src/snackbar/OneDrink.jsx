function OneDrink({ drink }) {
  return (
    <div>
      <h5>{drink.name}</h5>
      <img src={drink.image} alt={drink.name} style={{ width: 200 }} />
    </div>
  );
}

export default OneDrink;
