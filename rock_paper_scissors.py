import random

player_wins = 0 
computer_wins = 0
draw = 0

choices = ["rock", "paper", "scissors"]

while True: 
    player_input = input("Type Rock/Paper/Scissors or Q to quit the game: ").lower()
    if player_input == "q":
        break

    if player_input not in choices:
        print("Please choose either... Rock, Paper or Scissors")
        continue

    random_number = random.randint(0, 2)
    computer_choice = choices[random_number]
    print("The Computer chose..." + computer_choice + ".")

    if player_input == computer_choice:
        print("Draw!")
        draw = draw + 1
        

    elif player_input == "rock" and computer_choice == "scissors":
        print("Player Won!")
        player_wins = player_wins + 1
        

    elif player_input == "paper" and computer_choice == "rock":
        print("Player Won!")
        player_wins = player_wins + 1
        

    elif player_input == "scissors" and computer_choice == "paper":
        print("Player Won!")
        player_wins = player_wins + 1
        

    else:
        print("Computer Won!")
        computer_wins = computer_wins + 1

    print("Player Won: " + str(player_wins) + " times.")
    print("The Computer Won: " + str(computer_wins) + " times.")
    print("Thank's for playing!")

    