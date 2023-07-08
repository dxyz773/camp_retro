import { useNavigate, useRouteError } from "react-router-dom";
function Error() {
  const navigate = useNavigate();
  const error = useRouteError();
  console.log(error);

  return (
    <div>
      <h2>🫤 Something went wrong...</h2>
      <p>{error.data || error.message}</p>
      <button onClick={() => navigate(-1)}>return to previous page⇦</button>
    </div>
  );
}

export default Error;
