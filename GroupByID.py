import secrets
import random
import time

# List of possible fish to catch
fishes = {
    "Goldfish": 5,
    "Trout": 10,
    "Bass": 15,
    "Catfish": 20,
    "Shark": 50
}

def display_welcome():
    print("Welcome to the Fishing Game!")
    print("Try to catch different types of fish to score points.")
    print("Good luck!")

def catch_fish():
    # Use secrets to select a fish securely
    fish_index = secrets.randbelow(len(fishes))  # Get a random index
    fish = list(fishes.keys())[fish_index]  # Select the fish based on index
    score = fishes[fish]
    print(f"You caught a {fish}! (Score: {score})")
    return score

def play_game():
    total_score = 0
    rounds = 5  # Number of fishing attempts

    for round in range(rounds):
        print(f"\nRound {round + 1}:")
        time.sleep(1)  # Simulate waiting time for fishing
        total_score += catch_fish()

    print(f"\nGame Over! Your total score is: {total_score}")

def main():
    display_welcome()
    play_game()

if __name__ == "__main__":
    main()
