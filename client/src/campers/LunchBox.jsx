import UserContext from "../context/UserContext";
import { useContext, useEffect } from "react";

function LunchBox() {
  const { user, updateUser } = useContext(UserContext);

  useEffect(() => {
    fetch("http://127.0.0.1:5555/check_session")
      .then((res) => res.json())
      .then((data) => updateUser(data));
  }, []);
  return (
    <div
      className="bg-cover bg-[url('https://images.unsplash.com/photo-1600160797457-f3194244bce3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80')]"
      style={{ height: "100vh" }}
    >
      <div className="flex flex-col p-12 bg-yellow-50 rounded-3xl bg-opacity-60 w-6/12">
        <div className="text-4xl ml-48 mb-10 font-semibold">
          <h3 className="tracking-wide">Lunchbox</h3>
        </div>
        <section className="flex gap-20 ml-10">
          <div className="flex flex-col">
            <div className="rounded-2xl px-4 bg-white mb-2 bg-opacity-80">
              <h4 className="text-2xl font-semibold">Snack</h4>
              <p className="text-md font-semibold mb-3">
                {user.lunch_box[0].snack.name}
              </p>
            </div>
            <img
              src={user.lunch_box[0].snack.image}
              alt={user.lunch_box[0].snack.name}
              width={200}
              className="shadow-xl rounded-3xl hover:scale-105 shadow-neutral-800 transition-all duration-300"
            />
          </div>
          <div className="flex flex-col">
            <div className="rounded-xl px-4 bg-white mb-2 bg-opacity-80">
              <h4 className="text-2xl font-semibold">Drink</h4>
              <p className="text-md font-semibold mb-3">
                {user.lunch_box[0].drink.name}
              </p>
            </div>
            <img
              className="shadow-xl rounded-3xl hover:scale-105 shadow-neutral-800 transition-all duration-300"
              src={user.lunch_box[0].drink.image}
              alt={user.lunch_box[0].drink.name}
              width={200}
            />
          </div>
        </section>
      </div>
    </div>
  );
}

export default LunchBox;
