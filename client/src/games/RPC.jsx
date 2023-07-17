import { useState } from "react";

function RPC() {
  const [message, setMessage] = useState("");
  const rpc = ["rock", "paper", "scissors"];

  function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }
  console.log(message);
  const rock = rpc[0];
  const paper = rpc[1];
  const scissors = rpc[2];

  function RPSGame(userChoice) {
    const computerGenerate = getRandomInt(3);
    const computerChoice = rpc[computerGenerate];
    const win = "You win!";
    const lose = "You lose!";
    console.log(`Computer choice: ${computerChoice}`);
    console.log(`User choice: ${userChoice}`);

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
        (computerChoice === "paper" && userChoice === " rock") ||
        (computerChoice === "rock" && userChoice === "scissors") ||
        (computerChoice === "scissors" && userChoice === "paper")
      ) {
        gameMessage = lose;
        return gameMessage;
      }
    };
    const test = drawMessage();

    console.log(test);
    return test;
  }

  return (
    <div>
      <h2>RPC</h2>
      <button
        className="ml-4"
        onClick={() => {
          setMessage(RPSGame(rock));
        }}
      >
        Rock
      </button>
      <button
        className="ml-4"
        onClick={() => {
          setMessage(RPSGame(paper));
        }}
      >
        Paper
      </button>
      <button
        className="ml-4"
        onClick={() => {
          setMessage(RPSGame(scissors));
        }}
      >
        Scissors
      </button>
      <p>{message ? message : "nothing here"}</p>
    </div>
  );
}

export default RPC;
