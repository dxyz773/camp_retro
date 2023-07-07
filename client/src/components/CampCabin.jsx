import { useLoaderData } from "react-router-dom";
function CampCabin() {
  const camper = useLoaderData();
  console.log(camper);
  return (
    <div>
      <p>Welcome to your camp cabin</p>
    </div>
  );
}

export default CampCabin;
