import { useNavigate } from "react-router-dom";
import { useState, useContext } from "react";
import { useFormik } from "formik";
import UserContext from "../context/UserContext";
import * as yup from "yup";

function Login() {
  const [error, setError] = useState(null);
  const navigate = useNavigate();
  const { updateUser } = useContext(UserContext);
  const schema = yup.object().shape({
    username: yup.string().required("Please enter a username"),
    password: yup.string().required("Please enter a password"),
  });

  const formik = useFormik({
    initialValues: { username: "", password: "" },
    validationSchema: schema,
    onSubmit: (values, actions) => {
      fetch("http://127.0.0.1:5555/login", {
        method: "POST",
        credentials: "include",
        headers: {
          "content-type": "application/json",
        },

        body: JSON.stringify(values),
      }).then((res) => {
        if (res.ok) {
          res.json().then((data) => {
            updateUser(data);
            actions.resetForm();
            navigate("/");
          });
        } else {
          res.json().then((err) => setError(err.message));
        }
      });
    },
  });
  return (
    <div
      className=" bg-cover bg-[url('https://images.unsplash.com/photo-1608805875444-e61e4c53c9d8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1325&q=80')]"
      style={{ height: "100vh" }}
    >
      <form onSubmit={formik.handleSubmit}>
        <div>
          <label htmlFor="username">Username: </label>
          <input
            type="text"
            name="username"
            id="username"
            value={formik.values.username}
            onChange={formik.handleChange}
            autoComplete="username"
            onBlur={formik.handleBlur}
            placeholder="Username here.."
          />
          {formik.touched.username && formik.errors.username ? (
            <h5 style={{ color: "red" }}>{formik.errors.username}</h5>
          ) : (
            ""
          )}
        </div>
        <div>
          <label htmlFor="login_password">Password: </label>
          <input
            type="password"
            name="password"
            id="login_password"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            placeholder="Password"
          />
          {formik.touched.password && formik.errors.password ? (
            <h5 style={{ color: "red" }}>{formik.errors.password}</h5>
          ) : (
            ""
          )}
        </div>
        <div>
          <input type="submit" value="Login" />
          {error ? <label style={{ color: "red" }}>{error}</label> : ""}
        </div>
      </form>
    </div>
  );
}

export default Login;
