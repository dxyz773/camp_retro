// ---------------------------------------------------
//                      API URL
// ---------------------------------------------------
const api_url = "http://127.0.0.1:5555";
// ---------------------------------------------------
//                      CAMPER
// ---------------------------------------------------
async function getCamper() {
  const res = await fetch(`${api_url}/campers`);

  if (!res.ok) throw Error("Failed to get campers");

  const data = await res.json();
  return data;
}
// -------------- LOADER ------------------------------
export async function campersLoader() {
  const camper = await getCamper();

  return camper;
}
// ---------------------------------------------------
//                      DRINK
// ---------------------------------------------------
async function getDrinks() {
  const res = await fetch(`${api_url}/drinks`);

  if (!res.ok) throw Error("Failed to get drinks");

  const data = await res.json();
  return data;
}
// -------------- LOADER ------------------------------
export async function drinksLoader() {
  const drinks = await getDrinks();
  return drinks;
}
// ---------------------------------------------------
//                      SNACK
// ---------------------------------------------------
async function getSnacks() {
  const res = await fetch(`${api_url}/snacks`);
  if (!res.ok) throw Error("Failed to get snacks");

  const data = await res.json();
  return data;
}
// -------------- LOADER ------------------------------
export async function snacksLoader() {
  const snacks = await getSnacks();
  return snacks;
}
