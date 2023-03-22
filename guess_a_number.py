import random
computer_number = random.randint(1, 100)
while True:
    player_input = input("Guess the random number (1-100):  ")
    if not player_input.isdigit():
        print("Invalid input!Try again!")
        continue
    player_number = int(player_input)

    if player_number == computer_number:
        print("You guessed it !Congratulations!")
        break
    elif player_number > computer_number:
        print("Too High!")
    else:
        print("Too Low!")
