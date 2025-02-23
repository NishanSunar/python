#function with one parameter
# def greet(name):
#     print(f"Namaste {name}")
#     print("How are you?")
#     print("Are you all right?")
# name = input("Enter your name:")
# greet(name)

#function with two parameter
def greet(location,name) :
    print(f"Hello {name}. How is it in {location}")
    

greet(name="Nishan",location = "itahari")#keyword argument(value of name and location will be same even the place is changed.)
