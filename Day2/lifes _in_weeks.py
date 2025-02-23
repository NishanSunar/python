# Create a program using maths and f-String that tells us how many days , weeks , months we have left if we live until 90 years old.
#1 years = 365 days
#1 years = 52 weeks
#1 years = 12 months

age = input("Enter your current age: ")
int_age = int(age)
years_left = 90-int_age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")