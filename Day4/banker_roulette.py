import random
names = input("Enter everybody names seperated by comma.")
name = names.split(", ")  #this will split the list seperated by comma
# x = len(name)
# contributor = random.randint(0, x-1)
# print(f"{name[contributor]} will pay the bill...")
contributor = random.choice(name)
print(f"{contributor} will pay the bill...")
