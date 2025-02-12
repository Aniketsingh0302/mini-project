import random 

print("welcome to the game of chance")
l=["snake","water","gun"]
while True:
    userchoice=int(input("enter your choice 1 for snake,2 for water,3 for gun,5 for exit:--->"))
    computerchoice=random.choice(l)
    if userchoice==5:
        break
    elif userchoice==1 and computerchoice=="snake":
        print("its a tie")
    elif userchoice==1 and computerchoice=="water":
        print("you lose computer wins")
    elif userchoice==1 and computerchoice=="gun":
        print("you win computer loses")
        break
    elif userchoice==2 and computerchoice=="snake":
        print("you win computer loses")
        break
    elif userchoice==2 and computerchoice=="water":
        print("its a tie")
    elif userchoice==2 and computerchoice=="gun":
        print("you lose computer wins")
    elif userchoice==3 and computerchoice=="snake":
        print("you lose computer wins")
    elif userchoice==3 and computerchoice=="water":
        print("you win computer loses")
        break
    elif userchoice==3 and computerchoice=="gun":
        print("its a tie")
    else:
        print("invalid input")

