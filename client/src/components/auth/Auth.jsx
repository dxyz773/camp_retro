import { useFormik } from "formik";
import * as yup from "yup";
import { useNavigate } from "react-router-dom";
function Auth() {
  const navigate = useNavigate();
  const schema = yup.object().shape({
    username: yup.string().required("Username is required"),
    password: yup.string().required("Password is required"),
    camper_name: yup.string().required("Camper name is required"),
  });

  const formik = useFormik({
    initialValues: { username: "", password: "", camper_name: "" },
    validationSchema: schema,
    onSubmit: (values) => {
      fetch("http://127.0.0.1:5555/signup", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(values),
      }).then((res) => {
        if (res.ok) {
          res.json().then((data) => {
            console.log(data);
            navigate("/camp-cabin");
          });
        } else {
          console.log("Submission error");
        }
      });
    },
  });
  return (
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
          <button>Signup</button>
        </div>
      </form>
    </div>
  );
}

export default Auth;
