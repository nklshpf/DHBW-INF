import random

user_input = input("Enter a choice (rock, paper, scissors):")
possible_input = ["rock","paper","scissors"]
computer_input = random.choice(possible_input)
print(f"\n You chose {user_input}. Computer chose {computer_input}")
if user_input == computer_input :
    print(f"\n It's a tie, both players chose {user_input}")
elif user_input == "rock":
    if computer_input == "scissors":
        print(f"\n Rock wins against Scissors! You win!")
    else:
        print(f"\n Paper wins against Rock! You lost!")
elif user_input == "paper":
    if computer_input == "rock":
        print(f"\n Paper wins against Rock! You win!")
    else:
        print(f"\n Scissors wins against Paper! You lost!")
elif user_input == "scissors":
    if computer_input == "paper":
        print(f"\n Scissors wins against Paper! You win!")
    else:
        print(f"\n Rock wins against Scissors! You lost!")


