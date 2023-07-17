const rpc = ["rock", "paper", "scissors"];
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const computerGenerate = getRandomInt(3);

const rock = rpc[0];
const paper = rpc[1];
const scissors = rpc[2];

export function RPSGame() {
  const computerChoice = rpc[computerGenerate];
  console.log(computerChoice);

  // if (computerChoice === userChoice) {
  //   console.log("It's a draw!");
  // }
}
