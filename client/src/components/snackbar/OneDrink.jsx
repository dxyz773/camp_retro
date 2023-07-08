function OneDrink({ drink }) {
  return (
    <div style={{ display: "inline-block" }}>
      <p>{drink.name}</p>
      <img
        src={drink.image}
        alt={drink.name}
        width="200"
        style={{ borderRadius: "100%" }}
      />
    </div>
  );
}

export default OneDrink;
