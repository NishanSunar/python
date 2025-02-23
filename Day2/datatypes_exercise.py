#Write a program that adds the digits in a 2 digits number . e.g if the input was 35 , then the output should be 3 + 5 = 8
num = input("Enter the two digit number: ")

first_digit = num[0]
second_digit = num[1]

result = int(first_digit) + int(second_digit)
print(first_digit  + " + " + second_digit + " = " + str(result) )
