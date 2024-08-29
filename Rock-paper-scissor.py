import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie."
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        return "You win!"
    else:
        return "Computer wins."

def play_game():
    choices = ["stone", "paper", "scissors"]
    
    while True:
        user_choice = input("Choose stone, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}.")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing. Goodbye!")
            break

play_game()
