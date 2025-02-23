print("welcome to the rollercoaster....")
height = int(input("Enter your Height(cm) : "))

if height >= 120 :
    print("You can ride the rollercoaster..")
else:
    print("SORRY! ,You can't ride the rollercoaster...")


    #Nested if statement
if height >= 120 :
    print("You can ride the rollercoaster..")
    age = int(input("Enter your age : "))
    if age < 12 :
        print("You should pay 5$")
    elif age >= 18:
        print("You should pay 12$")
    else :
        print("you should pay 7$")

else:
    print("SORRY! ,You can't ride the rollercoaster...")



