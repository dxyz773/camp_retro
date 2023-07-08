import { Form } from "react-router-dom";
function Auth() {
  return (
    <div>
      <h3> Signup for Camp</h3>
      <Form method="POST">
        <div>
          <label htmlFor="username">Username:</label>
          <input type="text" name="username" id="username" />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input type="password" name="password" id="password" />
        </div>
        <div>
          <label htmlFor="camper_name">Camper Name:</label>
          <input type="text" name="camper_name" id="camper_name" />
        </div>
        <div>
          <button>Signup</button>
        </div>
      </Form>
    </div>
  );
}

export default Auth;
