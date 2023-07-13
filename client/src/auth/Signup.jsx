import { useNavigate, NavLink } from "react-router-dom";
import { useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function Signup({ updateUser }) {
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const schema = yup.object().shape({
    username: yup.string().required("Please enter a username"),
    password: yup.string().required("Please enter a password"),
    camper_name: yup.string().required("Please enter a camper name"),
  });

  const formik = useFormik({
    initialValues: { username: "", password: "", camper_name: "" },
    validationSchema: schema,
    onSubmit: (values, actions) => {
      fetch("http://127.0.0.1:5555/signup", {
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
    <div>
      <form onSubmit={formik.handleSubmit}>
        <div>
          <label htmlFor="username">Username: </label>
          <input
            type="text"
            name="username"
            value={formik.values.username}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          {formik.touched.username && formik.errors.username ? (
            <h5 style={{ color: "red" }}>{formik.errors.username}</h5>
          ) : (
            ""
          )}
        </div>
        <div>
          <label htmlFor="password">Password: </label>
          <input
            type="password"
            name="password"
            value={formik.values.password}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          {formik.touched.password && formik.errors.password ? (
            <h5 style={{ color: "red" }}>{formik.errors.password}</h5>
          ) : (
            ""
          )}
        </div>
        <div>
          <label htmlFor="camper_name">Camper Name</label>
          <input
            type="text"
            name="camper_name"
            value={formik.values.camper_name}
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
          />
          {formik.touched.camper_name && formik.errors.camper_name ? (
            <h5 style={{ color: "red" }}>{formik.errors.camper_name}</h5>
          ) : (
            ""
          )}
        </div>
        <div>
          <input type="submit" value="signup" />
          {error ? <label style={{ color: "red" }}>{error}</label> : ""}
        </div>
      </form>
      <div>
        <button>
          <NavLink to="/login">Already have an account? Login here:</NavLink>
        </button>
      </div>
    </div>
  );
}

export default Signup;
