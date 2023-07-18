import { NavLink } from "react-router-dom";

function Games() {
  return (
    <div className="bg-cover bg-black" style={{ height: "100vh" }}>
      <img
        src="https://images.unsplash.com/photo-1517859713810-5345f411b5f7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2670&q=80"
        style={{ width: 700, marginLeft: "auto", marginRight: "auto" }}
      />
      <button className="text-neutral-50">
        <NavLink to="/rock-paper-scissors">Rock Paper Scissors</NavLink>
      </button>
    </div>
  );
}

export default Games;
