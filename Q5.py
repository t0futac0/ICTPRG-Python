## Write a program that asks the user for the salary and the time in the job. 
## The minimum salary for the sanction of a bank loan is an annual salary of $50000 
## and the person has to be on the current job for at least 3 years. 
## The program should decide whether the person can be given a loan. 
## Use nested if statement with else. 

# Get income
# Get years worked

#Check income > 50k
    #Check time worked >= 3y
        #approved
    #else
        #not enough time
#not enough income         

annual_salary = int(input("Please enter your annual salary "))
time_worked = int(input("Please enter your time at the company "))

if annual_salary >= 50000 and time_worked >= 3:
    print("Congratulations! Loan approved")

else:
    if annual_salary < 50000 and time_worked >=3:
        print:("Not enough income, loan denied!")

    if annual_salary > 50000 and time_worked <=3:
        print("Not enough time, loan denied!")

    if annual_salary < 50000 and time_worked >3:
        print("Not enough income, loan denied!")


    
