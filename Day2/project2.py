#TIP CALCULATOR
#if the bill was $150.00 , split between 5 peoples , with 12% tip.
#each person should pay (150.00 / 5) * 1.12

print("Welcome to the tip calculator")
bill = input("Enter the total bill : ")
tip_perc = input("Tip percentage you would you like to give : ")
people = input("Number of people to split : ")

tip_amount = float(tip_perc) / 100 * float(bill)
total_bill = float(bill) + tip_amount 
split_bill = total_bill / int(people)
print(f"Each person should pay: ${round(split_bill,2)}")