import random

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return "It's a tie!"
    elif (
        (user_action == "rock" and computer_action == "scissors") or
        (user_action == "paper" and computer_action == "rock") or
        (user_action == "scissors" and computer_action == "paper")
    ):
        return "You win!"
    else:
        return "You lose."

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    
    print("You chose", user_action)
    print("Computer chose", computer_action)
    
    result = determine_winner(user_action, computer_action)
    print(result)

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
