# This is a simple implementation of the Rock, Paper, Scissors game in Python. 
import random
print("🎮 Welcome to Rock, Paper, Scissors!")
print("Type 'q' to quit.\n")

options = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice.lower()=="q":
        print("Bye Bye")
        break
    elif user_choice not in options:
        print("❌ Invalid choice. Please try again.")
        continue
    computer_choice=random.choice(options)
    print(f"The computer thought of: {computer_choice}")
    if computer_choice==user_choice:
        print("This is a tie")
    elif(
    computer_choice=="rock" and user_choice=="paper" or
    computer_choice=="paper" and user_choice=="scissors" or
    computer_choice=="scissors" and user_choice=="rock"
    
    ):
        print(f"You Won ma man the computer choice was {computer_choice}")
    else:
        print("The computer won friendo")

    print("-" * 40)