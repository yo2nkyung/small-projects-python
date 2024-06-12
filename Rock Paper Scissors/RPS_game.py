import random

def get_user_choice():
    while True:
        user_choice = input("Choose among 'rock', 'scissors', 'paper': ")
        if user_choice in ['rock', 'scissors', 'paper']:
            return user_choice
        else:
            print("Invalid input. Please choose 'rock', 'scissors', or 'paper'.")
    

def get_computer_choice():
    computer_choice = random.choice(['rock', 'scissors', 'paper'])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == "scissor" and computer_choice == "rock") or
          (user_choice == "rock" and computer_choice == "paper") or
          (user_choice == "paper" and computer_choice == "scissor")):
        return "COMPUTER wins!"
    else:
        return "USER wins!"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print("\n---GAME RESULT---")
    print(f"user: {user_choice}")
    print(f"computer: {computer_choice}")
    print(f"result: {result}\n")

while True:
    play_game()
    user_input = input("Still want to play? (y/n): ").lower()
    if user_input != 'y':
        break