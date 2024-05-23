import random

print("WELCOME TO THE NUMBER GUESSING GAME")
start = input("To start the game type YES, and to exit the game type NO : ").strip()

if start == "YES":
    

    lower = int(input("Enter the lower bound : "))
    upper = int(input("Enter the upper bound : "))

    x = random.randint(lower,upper)
    chance = round(upper-lower)/2 
    print("you have only ", chance, " chances to guess the number" )
    count = 0
    while count<chance:
        count+=1
        guess = int(input("Guess the number : "))

        if guess == x:
            print("Hurray! you guessed the correct number in ", count, " trials!")
            break
        elif x>guess:
            print("you guessed a smaller number, try again") 

        elif x<guess:
            print("you guessed a bigger number, try again")

    if count>=chance:
        print("All your chances are over, You lost the game.")      

elif start =="NO":
    print("Thankyou for wasting your time")
    exit

else:
    print("Please enter YES/NO")