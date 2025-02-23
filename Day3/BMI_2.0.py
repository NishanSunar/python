height = float(input("Enter your Height(m) : "))
weight = float(input("Enter your Weight(kg) : "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, You are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, You are obese.")
else :
    print(f"Your bmi is {bmi}, You are  clinically obese.")