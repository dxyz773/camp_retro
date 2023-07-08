import { useFormik } from "formik";
import * as yup from "yup";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
function Auth() {
  const [signup, setSignup] = useState(true);
  const [error, setError] = useState(null);

  const api_url = "http://127.0.0.1:5555";
  const navigate = useNavigate();

  function toggleSignup() {
    setSignup((prev) => !prev);
  }
  const schema = yup.object().shape({
    username: yup.string().required("Username is required"),
    password: yup.string().required("Password is required"),
    camper_name: yup.string().required("Camper name is required"),
  });

  const formik = useFormik({
    initialValues: { username: "", password: "", camper_name: "" },
    validationSchema: schema,
    onSubmit: (values, actions) => {
      fetch(signup ? `${api_url}/signup` : `${api_url}/login`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(values),
      }).then((res) => {
        if (res.ok) {
          res.json().then((data) => {
            console.log(data);
            actions.resetForm();
            navigate("/camp-cabin");
          });
        } else {
          res.json().then((err) => setError(err.message));
        }
      });
    },
  });
  return (
    <div>
      {signup ? (
        <div>
          <h3> Signup for Camp</h3>
          <form onSubmit={formik.handleSubmit}>
            <div>
              <label htmlFor="username">Username:</label>
              <input
                onChange={formik.handleChange}
                type="text"
                name="username"
                id="username"
                value={formik.values.username}
                onBlur={formik.handleBlur}
              />
              {formik.touched.username && formik.errors.username ? (
                <h5 style={{ color: "red" }}>{formik.errors.username}</h5>
              ) : (
                ""
              )}
            </div>
            <div>
              <label htmlFor="password">Password:</label>
              <input
                onChange={formik.handleChange}
                type="password"
                name="password"
                id="password"
                value={formik.values.password}
                onBlur={formik.handleBlur}
              />
              {formik.touched.password && formik.errors.password ? (
                <h5 style={{ color: "red" }}>{formik.errors.password}</h5>
              ) : (
                ""
              )}
            </div>
            <div>
              <label htmlFor="camper_name">Camper Name:</label>
              <input
                onChange={formik.handleChange}
                type="text"
                name="camper_name"
                id="camper_name"
                value={formik.values.camper_name}
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
        </div>
      ) : (
        <div>
          <h3>Camper Login</h3>
          <form className="form" onSubmit={formik.handleSubmit}>
            <div>
              <label>Username</label>

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
              <label>Password</label>

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
              <input type="submit" value="login" />
              {/* 9c. use conditional rendering to display the error to user */}
              {error ? <label style={{ color: "red" }}>{error}</label> : ""}
            </div>
          </form>
        </div>
      )}

      <section>
        <p>{signup ? "Already have an account?" : "Not a member?"}</p>
        <button className="button" onClick={toggleSignup}>
          {signup ? "Login" : "Sign Up"}
        </button>
      </section>
    </div>
  );
}

export default Auth;
