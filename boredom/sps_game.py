import random

print("WELCOME TO STONE PAPER SCISSOR GAME!")
tuple=("stone", "paper", "scissor")

user = input("Enter stone, paper or scissor : ")
if user not in tuple:
    print("enter a valid option")

comp = random.choice(tuple)
print("You chose :", user ," and computer chose :", comp)
if user == comp:
    print("it is a tie!")
elif (user == "paper" and comp == "stone") or (user == "stone" and comp == "scissor") or (user == "scissor" and comp == "paper"):
    print("Hurray, you won!")
else:
    print("Better luck next time")