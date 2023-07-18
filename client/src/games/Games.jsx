import { NavLink } from "react-router-dom";

function Games() {
  return (
    <div
      className="bg-cover bg-[url('https://images.unsplash.com/photo-1598804033652-7b06300a73a6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80')]"
      style={{ height: "100vh" }}
    >
      <button className="text-neutral-50">
        <NavLink to="/rock-paper-scissors">Rock Paper Scissors</NavLink>
      </button>
    </div>
  );
}

export default Games;
