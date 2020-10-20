#Python String Manipulation
#Write a program that asks the user for their full name, splits it up into words and outputs each word on a new line. 
#For names with 2 words (eg, 'Fred Frank') this would output Fred, then frank on two lines.

full_name = input("Please enter your full name ")
name_list = full_name.split()

for x in name_list:
    print(x)