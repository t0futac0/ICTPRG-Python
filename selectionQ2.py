## Write a program that asks the user for their year of birth, 
## Checks if they are of legal drinking age
## and tells the user to come into the bar. 

age_verification = int(input("What is your year of birth? "))

if age_verification >= 2002:
    print("Do a U-Turn!")
else:
    print("Please come straight through to the bar!")