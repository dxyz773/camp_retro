function Lunchbox({ user }) {
  const { camper_name, username, lunch_box } = user;
  return (
    <div>
      <h2>Luncbox</h2>
      <h4>{username}</h4>
      <h4>{camper_name}</h4>
    </div>
  );
}

export default Lunchbox;
