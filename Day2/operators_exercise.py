#Body Mass Index calculator (BMI calculator)

height = input("Enter your Height: ")
weight = input("Enter your Weight: ")

BMI = float(weight) / float(height) ** 2
print("Your BMI is " + str(int(BMI)))