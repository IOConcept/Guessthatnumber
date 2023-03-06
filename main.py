import random

attempts = 0
while True:
    print("Guess the Number")
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
            attempts -= 1 # Decrement attempts count
            continue

        if guess < range_start or guess > range_end:
            print(f"Invalid guess. Guess must be between {range_start} and {range_end}")
            attempts -= 1 # Decrement attempts count
            continue

        if guess == number:
            print(f"Congratulations, {name}! You guessed the number in {attempts} attempts!")
            if cheat:
                print("But you cheated!")
            leaderboard.append((name, attempts, option))
            attempts = 0 # Reset attempts count for next game
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
