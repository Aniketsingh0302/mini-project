import random

Target= random.randint(1,100)
while True:
    userchoice= input("Guess the number between 1 and 100 or enter Q for exit from the game: ")
    if userchoice.upper() == "Q":
        print("Thanks for playing the game. The number was: ", Target)
        break
    userchoice = int(userchoice)
    if userchoice == Target:
        print("Congratulations! You guessed the number correctly.")
        break
    elif(userchoice>Target):
        print("Your guess is too high. Try again!")
    else:
        print("Your guess is too low. Try again!")

print("<----GAMEOVER---->")