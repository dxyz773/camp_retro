import { useState } from "react";

function RPC() {
  const rpc = ["rock", "paper", "scissors"];
  const [message, setMessage] = useState("");
  const [userC, setUserC] = useState("");
  const [computerC, setComputerC] = useState("");

  function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

  const rock = rpc[0];
  const paper = rpc[1];
  const scissors = rpc[2];

  const rockInfo = {
    image:
      "https://nationaltoday.com/wp-content/uploads/2021/08/National-Pet-Rock-Day.jpg",
    styling: "rounded-3xl w-50 h-40 py-2 hover:-translate-y-3",
  };
  const paperInfo = {
    image:
      "https://i.pinimg.com/originals/57/c5/9f/57c59f6cd9d050ee155f5ce9c905b028.jpg",
    styling: "rounded-3xl w-50 h-40 py-2 hover:-translate-y-3",
  };
  const scissorsInfo = {
    image:
      "https://cdn11.bigcommerce.com/s-sdq9gkoc6f/images/stencil/500x659/products/531/403/Amzn-728-website__61779.1630673176.jpg?c=2",
    styling: "rounded-3xl w-60 py-2 hover:-translate-y-3",
  };

  function RPSGame(userChoice) {
    //-------------------------------------------------------
    // Generate computer choice
    //-------------------------------------------------------
    const computerGenerate = getRandomInt(3);
    const computerChoice = rpc[computerGenerate];
    //-------------------------------------------------------
    // Win and Lose messages
    //-------------------------------------------------------
    const win = "You win!";
    const lose = "You lose!";
    // console.log(`Computer choice: ${computerChoice}`);
    // console.log(`User choice: ${userChoice}`);
    //-------------------------------------------------------
    // Set User Choice state
    //-------------------------------------------------------

    if (userChoice === "rock") {
      setUserC(rockInfo);
    } else if (userChoice === "paper") {
      setUserC(paperInfo);
    } else if (userChoice === "scissors") {
      setUserC(scissorsInfo);
    }
    //-------------------------------------------------------
    // Set Computer Choice state
    //-------------------------------------------------------
    if (computerChoice === "rock") {
      setComputerC(rockInfo);
    } else if (computerChoice === "paper") {
      setComputerC(paperInfo);
    } else if (computerChoice === "scissors") {
      setComputerC(scissorsInfo);
    }
    //-------------------------------------------------------
    // Compute game Winner and Loser
    //-------------------------------------------------------
    let drawMessage = () => {
      let gameMessage;
      if (computerChoice === userChoice) {
        gameMessage = "It's a draw!";
        return gameMessage;
      } else if (
        (userChoice === "paper" && computerChoice === "rock") ||
        (userChoice === "rock" && computerChoice === "scissors") ||
        (userChoice === "scissors" && computerChoice === "paper")
      ) {
        gameMessage = win;
        return gameMessage;
      } else if (
        (computerChoice === "paper" && userChoice === "rock") ||
        (computerChoice === "rock" && userChoice === "scissors") ||
        (computerChoice === "scissors" && userChoice === "paper")
      ) {
        gameMessage = lose;
        return gameMessage;
      }
    };
    const test = drawMessage();

    return test;
  }

  return (
    <div>
      <h2 className="text-3xl font-semibold text-neutral-800 mr-4 tracking-wide uppercase text-center mb-14">
        Rock Paper Scissors
      </h2>

      <section className="flex justify-evenly mb-6">
        <div>
          {userC ? (
            <img
              src={userC.image}
              alt="User Choice"
              className={userC.styling}
            />
          ) : null}
        </div>
        <p className="text-5xl font-bold uppercase text-blue-9">
          {message
            ? message
            : "Click the ROCK, PAPER or SCISSORS button to play! 👇🏾"}
        </p>

        <div>
          {computerC ? (
            <img
              src={computerC.image}
              alt="Computer Choice"
              className={computerC.styling}
            />
          ) : null}
        </div>
      </section>
      <div className="flex justify-between">
        <p className=" bg-neutral-50 bg-opacity-50 uppercase py-2 px-5 rounded-xl ml-44">
          Your choice
        </p>
        <p className=" bg-neutral-50 bg-opacity-50 uppercase py-2 px-5 rounded-xl mr-36">
          Computer's Choice
        </p>
      </div>

      <div className="flex justify-center pb-10 gap-7 mt-16">
        <button
          className="bg-green-500 rounded-2xl px-20 py-4 mt-3 hover:bg-green-400 transition-all duration-300 shadow-xl shadow-neutral-800 active:-scale-50"
          onClick={() => {
            setMessage(RPSGame(rock));
          }}
        >
          Rock
        </button>
        <button
          className=" bg-blue-500 rounded-2xl px-20 py-4 mt-3 hover:bg-blue-400 transition-all duration-300 shadow-xl shadow-neutral-800"
          onClick={() => {
            setMessage(RPSGame(paper));
          }}
        >
          Paper
        </button>
        <button
          className=" bg-pink-500 rounded-2xl px-20 py-4 mt-3 hover:bg-pink-400 transition-all duration-300 shadow-xl shadow-neutral-800"
          onClick={() => {
            setMessage(RPSGame(scissors));
          }}
        >
          Scissors
        </button>
      </div>
    </div>
  );
}

export default RPC;
