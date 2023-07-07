import { useLoaderData } from "react-router-dom";
function Snacks() {
  const snacks = useLoaderData();
  const allSnacks = snacks.map((snack) => (
    <div key={snack.id} style={{ display: "inline-block" }}>
      <p>{snack.name}</p>
      <img
        src={snack.image}
        alt={snack.name}
        width="200"
        style={{ borderRadius: "100%" }}
      />
    </div>
  ));
  return (
    <div>
      <p>Yummy Snacks</p>
      {allSnacks}
    </div>
  );
}

export default Snacks;
