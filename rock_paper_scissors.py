import random

choices = ["rock", "paper", "scissors"]

# Reset points
points = 0
print(f"YOU HAVE {points} POINTS!")
opponent_points = 0            

# Get the user to choose how many rounds (best of x). Only odd numbers can be chosen.
best_of = 0
best_of = int(input("Best out of? "))
while True:
    try:
        while best_of % 2 == 0:
            print("Best of must be odd, please try again.")
            best_of = int(input("Best out of? "))
        break
    except:
        print("Invalid Input, please try again.")


# Play as many rounds it takes until there are as many points as there are rounds in 'best_of'
for round in range(best_of):
    print("-------------------------------------------")
    while True:
        # Player choice
        choice = input("""Rock, Paper or Scissors?
R = Rock
P = Paper
S = Scissors
""").lower()
        print("-------------------------------------------")

        # Opponent_choice. Rock = 0, Paper = 1, Scissors = 2
        random_choice = random.randrange(0,3)
        opponent_choice = choices[random_choice]

        # If not rock/paper/scissors - retry
        if choice not in ["rock", "paper", "scissors", "r", "p", "s"]:
            continue
        # Rock
        elif choice in ["rock", "r"]:
            print("You chose ROCK")
            if opponent_choice == "rock":
                print("You both chose ROCK")
                print("It's a draw. Nobody gets a point.")
                continue
            elif opponent_choice == "paper":
                print("Your opponent chose PAPER!")
                print("You lose! Opponent gets +1 point.")
                opponent_points += 1
                break
            elif opponent_choice == "scissors":
                print("Your opponent chose SCISSORS!")
                print("You Win! You get +1 point!")
                points += 1
                break
        # Paper
        elif choice in ["paper", "p"]:
            print("You chose PAPER")
            if opponent_choice == "paper":
                print("You both chose PAPER")
                print("It's a draw. Nobody gets a point.")
                continue
            elif opponent_choice == "scissors":
                print("Your opponent chose SCISSORS!")
                print("You lose! Opponent gets +1 point.")
                opponent_points += 1
                break
            elif opponent_choice == "rock":
                print("Your opponent chose ROCK!")
                print("You Win! You get +1 point!")
                points += 1
                break
        # Scissors
        elif choice in ["scissors", "s"]:
            print("You chose SCISSORS")
            if opponent_choice == "scissors":
                print("You both chose SCISSORS")
                print("It's a draw. Nobody gets a point.")
                continue
            elif opponent_choice == "rock":
                print("Your opponent chose ROCK!")
                print("You lose! Opponent gets +1 point.")
                opponent_points += 1
                break
            elif opponent_choice == "paper":
                print("Your opponent chose PAPER!")
                print("You Win! You get +1 point!")
                points += 1
                break
        
    # Print Score
    print(f"YOU: {points}")
    print(f"OPP: {opponent_points}")

    # Print outcome
    if points > opponent_points:
        print("YOU WIN!")
        print(f"FINAL SCORE: {points}-{opponent_points}")
    elif opponent_points > points:
        print("YOU LOSE!")
        print("GAME OVER!")