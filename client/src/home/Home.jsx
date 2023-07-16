import { NavLink } from "react-router-dom";

function Home() {
  return (
    <div
      className=" bg-cover bg-[url('https://images.unsplash.com/photo-1501555088652-021faa106b9b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1473&q=80')]"
      style={{ height: "100vh" }}
    >
      <h1
        className="text-5xl text-yellow-500 font-semibold text-center"
        style={{ paddingTop: "50px" }}
      >
        camp Retro
      </h1>
      <button
        className="bg-yellow-400 hover:bg-yellow-300 rounded-3xl py-3 px-6 shadow-xl"
        style={{
          display: "flex",
          marginLeft: "auto",
          marginRight: "auto",
          marginTop: "80px",
        }}
      >
        <NavLink to="/login">Login</NavLink>
      </button>
    </div>
  );
}

export default Home;
