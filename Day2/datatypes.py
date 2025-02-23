#datatypes

#string 
print("Nishan"[0])  #this print the 1st character of the string "Nishan"



#Type error


# length = len("Nishan")
# print("your name has " + length + "characters.")
#this gives error


# Solution (type conversion)
length = len("Nishan")
new_length = str(length)
print("your name has " + new_length + " characters.")


a = 123
print(type(a))
a = float(123)
print(type(a))