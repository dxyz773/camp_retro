import RPC from "./RPC";

function Games() {
  return (
    <div
      className="bg-cover bg-[url('https://images.unsplash.com/photo-1598804033652-7b06300a73a6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80')] pt-28"
      style={{ height: "100vh" }}
    >
      <div
        className="bg-yellow-300 bg-opacity-70 pl-12 pr-14 pt-8 "
        style={{ marginLeft: "auto", marginRight: "auto" }}
      >
        <RPC />
      </div>
    </div>
  );
}

export default Games;
