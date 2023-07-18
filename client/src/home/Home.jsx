import { NavLink } from "react-router-dom";

function Home() {
  return (
    <div
      className=" bg-cover bg-[url('https://images.unsplash.com/photo-1501555088652-021faa106b9b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1473&q=80')]"
      style={{ height: "100vh" }}
    >
      <h1
        className="text-5xl text-yellow-400 font-semibold text-center"
        style={{ paddingTop: "50px" }}
      >
        camp Retro
      </h1>
      <div className="flex justify-center gap-20 mt-20 pr-4">
        <button
          className="bg-yellow-400 hover:bg-yellow-300 rounded-3xl py-3 px-12 shadow-xl transition-all duration-300"
          style={{
            display: "flex",
            marginTop: "80px",
          }}
        >
          <NavLink to="/login">Login</NavLink>
        </button>
        <button
          className="bg-orange-400 hover:bg-orange-300 rounded-3xl py-3 px-12 shadow-md transition-all duration-300 self-start"
          style={{
            display: "flex",
            marginTop: "80px",
          }}
        >
          <NavLink to="/signup">Signup</NavLink>
        </button>
      </div>
    </div>
  );
}

export default Home;
