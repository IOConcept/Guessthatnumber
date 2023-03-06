import random

while True:
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's play Guess the Number.")

    print("Enter the range of numbers to guess from:")
    print("1. 1 to 1000")
    print("2. 1 to 100000")
    print("3. 1 to 1000000")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        range_start = 1
        range_end = 1000
        option = "1 to 1000"
    elif choice == 2:
        range_start = 1
        range_end = 100000
        option = "1 to 100000"
    elif choice == 3:
        range_start = 1
        range_end = 1000000
        option = "1 to 1000000"

    leaderboard = []
    attempts = 0
    cheat = False
    number = random.randint(range_start, range_end)

    while True:
        guess = input("Guess the number (or 'q' to quit): ")
        attempts += 1

        if guess == 'q':
            print("Goodbye!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input, try again.")
            continue

        if guess == number:
            print(f"Congratulations, {name}! You guessed the number in {attempts} attempts!")
            if cheat:
                print("But you cheated!")
            leaderboard.append((name, attempts, option))
            break
        elif guess > number:
            print("Lower")
        elif guess < number:
            print("Higher")

        if not cheat and attempts == 10:
            print("You have reached 10 attempts, do you want to cheat? (y/n)")
            cheat_choice = input()
            if cheat_choice.lower() == 'y':
                cheat = True
                print(f"The number is {number}")
            else:
                print("Okay, keep guessing!")

    print("Leaderboard:")
    for entry in leaderboard:
        print(f"{entry[0]} guessed the number in {entry[1]} attempts for option {entry[2]}")
    print()

    restart_choice = input("Do you want to play again? (y/n): ")
    if restart_choice.lower() != 'y':
        print("Thanks for playing!")
        break

    file_name = f"{name}_{choice}.txt"
    with open(file_name, "w") as f:
        for entry in leaderboard:
            f.write(f"{entry[0]}, {entry[1]}, {entry[2]}\n")
    print(f"Leaderboard saved to {file_name}")
