import { useNavigate } from "react-router-dom";
import { useState, useContext } from "react";
import { useFormik } from "formik";
import UserContext from "../context/UserContext";
import * as yup from "yup";

function Signup() {
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
      fetch("/api/signup", {
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
            navigate("/camp-cabin");
          });
        } else {
          res.json().then((err) => setError(err.message));
        }
      });
    },
  });

  return (
    <div
      className=" bg-cover bg-[url('https://images.unsplash.com/photo-1509931801034-6fb72ce134f4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1698&q=80')]"
      style={{ height: "100vh" }}
    >
      <div className="flex flex-col p-12 bg-purple-200 rounded-3xl bg-opacity-80 w-6/12">
        <div className="text-4xl ml-32 mb-10 font-semibold">
          <h3 className="tracking-wide">🏕️🌲🌳 Signup 🌼🌻✌🏾</h3>
        </div>
        <div>
          <form onSubmit={formik.handleSubmit}>
            <div className="my-3">
              <label
                className="text-2xl font-semibold text-neutral-800 mr-4 tracking-wide"
                htmlFor="username"
              >
                Username:
              </label>
              <input
                type="text"
                name="username"
                id="username"
                value={formik.values.username}
                onChange={formik.handleChange}
                autoComplete="username"
                onBlur={formik.handleBlur}
                placeholder="Username here.."
                className="py-3 px-3 w-96 rounded-full placeholder:px-3 shadow-xl placeholder:text-neutral-600"
              />
              {formik.touched.username && formik.errors.username ? (
                <h5 style={{ color: "red" }}>{formik.errors.username}</h5>
              ) : (
                ""
              )}
            </div>
            <div>
              <label
                className="text-2xl font-semibold text-neutral-800 mr-4 tracking-wide"
                htmlFor="login_password"
              >
                Password:
              </label>
              <input
                type="password"
                name="password"
                id="login_password"
                value={formik.values.password}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                placeholder="password..."
                className="py-3 px-3 w-96 rounded-full placeholder:px-3 shadow-xl placeholder:text-neutral-600"
              />
              {formik.touched.password && formik.errors.password ? (
                <h5 style={{ color: "red" }}>{formik.errors.password}</h5>
              ) : (
                ""
              )}
            </div>
            <div style={{ marginLeft: "151px" }}>
              <input
                style={{ width: "382px" }}
                className="bg-yellow-400 rounded-2xl px-30 py-1 mt-3 hover:bg-yellow-300 transition-all duration-300 shadow-xl"
                type="submit"
                value="☮️ Signup"
              />
              {error ? <label style={{ color: "red" }}>{error}</label> : ""}
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Signup;
