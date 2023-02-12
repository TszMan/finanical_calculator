import math

print("Choose either 'investment' or 'bond' from the meun below to proceed: \n")
print("investment - to calculate the amount of interest you'll earn on your invesetment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# To avoid the effct of different capitalisation of inputting selection by user, 
# the input of required calculation 'investment' or 'bond' will be transformed into lower letters 
# and do the string comparison for conditional statement aftwerwards
cal = input().lower()

if cal == "investment":
    principal = float(input("The amount you are depositing: "))
    interest_rate = float(input("Interest rate (DO NOT INPUT WITH '%' SIGN): "))/100
    year = int(input("Number of year you plan on investing: "))
    interest = input("Do you want simple or compound interest? (Please enter simple/compound): ").lower()
    if interest == "simple":
        amount = principal*(1+interest_rate*year)
        print(f"The amount will be {amount}.")
    elif interest == "compound":
        amount = principal*math.pow(1+interest_rate, year)
        print(f"The amount will be {amount}.")
    else:
        print("You have enter an invalid input!")
elif cal == "bond":
    house_value = float(input("The present value of the house: "))
    interest_rate = float(input("Interest rate (DO NOT INPUT WITH '%' SIGN): "))/100
    month = int(input("Enter number of month you plan to take to repay the bond: "))
    amount = (interest_rate/12*house_value)/(1-math.pow(1+interest_rate/12, -month))
    print(f"The amount you have to repay each month will be {amount}")
else:
    print("You have enter an invalid input!")