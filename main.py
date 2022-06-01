from random import randint

#create a list of play options
#R for Rock
#P for Paper
#S for Scissors
t = ["R", "P", "S"]

print("Winning Rules of the Rock paper scissor game as follows: \n"
								+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
								+"paper vs scissor->scissor wins \n")
#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    print("Enter choice \n R for Rock \n P for paper \n S for scissor \n")
    player = input("Your Choice: ")
    print ('Player' + ' (' + player + ')' + ' ' + ':' + ' ' + 'CPU' +  ' (' + computer + ')')
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose! Computer wins")
        else:
            print("You win! Computer lost")
            break
    elif player == "P":
        if computer == "S":
            print("You lose! Computer wins")
        else:
            print("You win! Computer lost")
            break
    elif player == "S":
        if computer == "R":
            print("You lose! Computer wins")
        else:
            print("You win! Computer lost")
            break
    else:
        print("That's not a valid play. Check your choice!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]