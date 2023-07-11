import { useEffect, useState } from "react";
function Camp() {
  const [campUsers, setCampUsers] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:5555/users")
      .then((res) => res.json())
      .then((data) => setCampUsers(data));
  }, []);

  const allUsers = campUsers.map((user) => (
    <img
      key={user.id}
      src={user.image}
      style={{ width: 200, borderRadius: "30px" }}
    />
  ));
  return (
    <div>
      <h3>Camp retro entrance</h3>
      {allUsers}
    </div>
  );
}

export default Camp;
