# AIM: Calculating Simple Interest
# Coder:Talha Khan
# Date:15/01/26

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time Period in Years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
