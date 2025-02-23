import random
choice = int(input("What do you choose ? 0 for Rock, 1 for Paper or 2 for Scissors."))
comp = random.randint(0,2)
print(comp)
if choice >= 3 or choice < 0 :
    print("You type wrong input")
elif choice == 0 and comp == 2:
    print("You won!")
elif comp == 0 and choice == 2:
    print("You lose!")
elif (comp > choice):
    print("you lose!")
elif choice > comp:
    print("You won!")
elif(comp == choice):
    print("It's a draw")
