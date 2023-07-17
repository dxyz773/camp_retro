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
    console.log(`Computer choice: ${computerChoice}`);
    console.log(`User choice: ${userChoice}`);

    let drawMessage = () => {
      if (computerChoice === userChoice) {
        let gameMessage = "It's a draw!";
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
          RPSGame(rock);
        }}
      >
        Rock
      </button>
      <button
        className="ml-4"
        onClick={() => {
          setMessage(RPSGame(paper));
          console.log(message);
        }}
      >
        Paper
      </button>
      <button className="ml-4" onClick={() => RPSGame(scissors)}>
        Scissors
      </button>
      <p>{message ? message : "nothing here"}</p>
    </div>
  );
}

export default RPC;
