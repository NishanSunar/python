#adding even numbers starting from 1 to 100

sum = 0
for even in range(2, 101, 2):
    sum += even
print(f"The sum of the even numbers is {sum}")

#Another way
total = 0
for number in range(1, 101):
    if  number%2 == 0:
        total += number

print(f"The sum of the even numbers is {total}")