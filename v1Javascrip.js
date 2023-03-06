let name = prompt("Enter your name:");
alert(`Hello, ${name}! Let's play Guess the Number.`);

let rangeStart, rangeEnd, option;
let choice = parseInt(prompt("Enter the range of numbers to guess from:\n1. 1 to 1000\n2. 1 to 100000\n3. 1 to 1000000"));

if (choice === 1) {
  rangeStart = 1;
  rangeEnd = 1000;
  option = "1 to 1000";
} else if (choice === 2) {
  rangeStart = 1;
  rangeEnd = 100000;
  option = "1 to 100000";
} else if (choice === 3) {
  rangeStart = 1;
  rangeEnd = 1000000;
  option = "1 to 1000000";
} else {
  alert("Invalid input. Please choose 1, 2 or 3.");
  throw new Error("Invalid input");
}

let leaderboard = [];
let attempts = 0;
let cheat = false;
let number = Math.floor(Math.random() * (rangeEnd - rangeStart + 1)) + rangeStart;

while (true) {
  let guess = prompt("Guess the number (or 'q' to quit): ");
  attempts++;

  if (guess === 'q') {
    alert("Goodbye!");
    break;
  }

  guess = parseInt(guess);

  if (isNaN(guess) || guess < rangeStart || guess > rangeEnd) {
    alert(`Invalid input. Please enter a number between ${rangeStart} and ${rangeEnd}.`);
    attempts--;
    continue;
  }

  if (guess === number) {
    alert(`Congratulations, ${name}! You guessed the number in ${attempts} attempts!`);
    if (cheat) {
      alert("But you cheated!");
    }
    leaderboard.push([name, attempts, option]);
    break;
  } else if (guess > number) {
    alert("Lower");
  } else {
    alert("Higher");
  }

  if (!cheat && attempts === 10) {
    let cheatChoice = prompt("You have reached 10 attempts, do you want to cheat? (y/n)");
    if (cheatChoice.toLowerCase() === 'y') {
      cheat = true;
      alert(`The number is ${number}`);
    } else {
      alert("Okay, keep guessing!");
    }
  }
}

let leaderboardText = "Leaderboard:\n";
for (let i = 0; i < leaderboard.length; i++) {
  leaderboardText += `${leaderboard[i][0]} guessed the number in ${leaderboard[i][1]} attempts for option ${leaderboard[i][2]}\n`;
}
alert(leaderboardText);
