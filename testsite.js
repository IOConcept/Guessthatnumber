function startGame() {
    document.getElementById("gameDialog").style.display = "block";
}

function cancelGame() {
    document.getElementById("gameDialog").style.display = "none";
}

function guessNumber() {
    var name = document.getElementById("playerName").value;
    var option = document.getElementById("rangeOption").value;
    var guess = document.getElementById("guess").value;
    var attempts = document.getElementById("attempts").innerHTML;
    attempts++;

    if (guess == "") {
        alert("Please enter a number.");
        return;
    }

    if (guess < 1 || guess > getRange(option)) {
        alert("Please enter a number between 1 and " + getRange(option) + ".");
        return;
    }

    var number = Math.floor(Math.random() * getRange(option)) + 1;

    if (guess == number) {
        alert("Congratulations, " + name + "! You guessed the number in " + attempts + " attempts!");
        cancelGame();
    } else if (guess > number) {
        alert("Lower");
    } else if (guess < number) {
        alert("Higher");
    }

    document.getElementById("guess").value = "";
    document.getElementById("attempts").innerHTML = attempts;
}

function getRange(option) {
    if (option == 1) {
        return 1000;
    } else if (option == 2) {
        return 100000;
    } else if (option == 3) {
        return 1000000;
    }
}
