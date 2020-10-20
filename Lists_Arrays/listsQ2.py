# Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019
# The date will be printed like below:
# Date: 23
# Month : 08
# Year: 2019

enter_date = input("Please enter a date in DD/MM/YYYY \n")
input_date = enter_date.split('/')

print("Day: "+ input_date[0] + "\n" + "Month: "+ input_date[1] + "\n" + "Year: "+ input_date[2])
