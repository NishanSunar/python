# # #logic
# # count the number of times truelove occures in both of the name.
# #and sum no of true and also sum no of love in the name 
# and join both which gives the love persentage

name_1 = input("What is your name : ")
name_2 = input("What is their name : ")

name = name_1 + name_2
lower_name = name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
true = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together,")
else:
    print(f"Your score is {love_score}")