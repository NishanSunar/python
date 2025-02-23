#For loop

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
    print(fruits)
print("it's outside of the loop")

#for loop and range() function

for number in range(1, 11, 3):
    print(number)

#adding all the number starting from zero
total = 0
for number in range(1, 101):
    total += number
print(total)