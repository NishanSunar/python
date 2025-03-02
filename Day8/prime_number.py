# def prime(num):
#     count = 0
#     for number in range(1,num):
#         if num%number == 0:
#             count += 1
#     if count == 1:
#         print(f"{num} is prime.")
#     else :
#         print(f"{num} is not a prime number")
        
        
# num = int(input("Enter the number:"))
# prime(num)
def prime(num):
    is_prime = True
    for number in range(2,num):
        if num%number == 0:
            is_prime = False
    if  is_prime:
        print(f"{num} is prime.")
    else :
        print(f"{num} is not a prime number")
        
        
num = int(input("Enter the number:"))
prime(num)