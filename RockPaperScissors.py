from colorama import Fore, Back, Style
import random

#read playe's move
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_wins = 0
computer_wins = 0

#games are 3 out of 2
counter = 0
while counter < 3:
    counter += 1

    #write on the console what options the player can choose
    player_move = input(Fore.BLUE + "Chose [r]ock, [p]aper or [s]cissors: ")

    #turn the user input into one of our player moves options
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        #if user enters an invalid value
        raise SystemExit("Invalid Input. Try again...")

    #choose Computer's Move with random.randint
    computer_random_number = random.randint(1, 3)

    computer_move = ""

    #Choose the computer's random move
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    #write the random selection of the computer choice
    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
                (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You win!")
        player_wins += 1
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
    else:
        computer_wins += 1
        print(Fore.RED + "You lose!")

if player_wins >= 2:
    print(Fore.LIGHTCYAN_EX + Back.BLACK + Style.DIM + "Player beat the computer!!")
elif computer_wins >= 2:
    print(Fore.LIGHTMAGENTA_EX + Back.BLACK + Style.BRIGHT + "Computer beat the player!")
else:
    print(Fore.LIGHTWHITE_EX + Back.BLACK + Style.BRIGHT + "Game is draw.. Play again?")