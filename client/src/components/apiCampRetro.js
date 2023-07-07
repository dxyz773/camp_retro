const api_url = "http://127.0.0.1:5555";

async function getCamper() {
  const res = await fetch(`${api_url}/campers/1`);

  if (!res.ok) throw Error("Failed to get campers");

  const data = await res.json();
  return data;
}

export async function camperLoader() {
  const camper = await getCamper();
  return camper;
}
