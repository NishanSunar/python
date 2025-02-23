#password generator
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','(',')','+']

print("Welcome to password generator!")
n_letters = int(input("Enter the number of letter you want in your password: "))
n_numbers = int(input("Enter the number of numbers you want in your password: "))
n_symbols = int(input("Enter the number of symbols you want in your password: "))

# password = ""
# for char in range(1, n_letters + 1):
#     password += random.choice(letters)
# for symbol in range(1, n_symbols + 1):
#     password += random.choice(symbols)
# for number in range(1, n_numbers + 1):
#     password += random.choice(numbers)
# print(password)

password_list = []
for char in range(1, n_letters + 1):
    password_list.append(random.choice(letters))
for symbol in range(1, n_symbols + 1):
    password_list.append(random.choice(symbols))
for number in range(1, n_numbers + 1):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
    
print(f"Your Password is {password}")
    
    

