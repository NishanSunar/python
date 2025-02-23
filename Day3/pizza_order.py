#Congratulation, you've got a job at python pizza. Your first job is to build an automatic pizza order program.
size = input("Enter the size of the pizza('S' for small ,'M' for medium, 'L' for large): ")
pepo = input("Do you want pepperoni? Y or N : ")
cheese = input("Do you want extra cheese? Y or N : ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepo == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

if cheese == "Y":
    bill += 1

print(f"Your final Bill is ${bill} .")
