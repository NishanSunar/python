#Program to check leap year
#logic
# divisible by 4
# divisible by 100 and also it should be divisible by 400
#if it is divisible by 100 and not divisible by 400 then is is not leap year


year = int(input("Enter the year : "))

if year % 4 == 0 :

    if year % 100 == 0 and year % 400 == 0 :
         print(f"Year {year} is a leap year.")
    else :
         print(f"Year {year} is a not a leap year.")
else :
     print(f"Year {year} is a not leap year.")