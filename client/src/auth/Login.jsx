import { useNavigate, NavLink } from "react-router-dom";
import { useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function Login({ token }) {
  const [error, setError] = useState(null);
  const navigate = useNavigate();

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
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": true,
        },

        body: JSON.stringify(values),
      }).then((res) => {
        if (res.ok) {
          res.json().then((data) => {
            console.log(data);
            sessionStorage.setItem("token", data.access_token);
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
    <div>
      {token && token !== undefined && token !== "" ? (
        <p>You are logged in</p>
      ) : (
        <p>Proceed to login</p>
      )}
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
      <div>
        <button>
          <NavLink to="/signup">{`Don't have an account yet? Signup here:`}</NavLink>
        </button>
      </div>
    </div>
  );
}

export default Login;
