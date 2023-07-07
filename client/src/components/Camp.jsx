import { useLoaderData } from "react-router-dom";
function Camp() {
  const campers = useLoaderData();
  console.log(campers);
  return <div>Welcome to camp!</div>;
}

export default Camp;
