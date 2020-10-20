#Write a program to ask the user for numbers, and then print any repeating numbers in a list. 
# Example:
#Enter a number: 5
#Enter a number: 2
#Enter a number: 6
#Enter a number: 98
#Enter a number: 7
#Enter a number: 6
#Enter a number: 5
#Enter a number: x
#Repeating numbers: [5, 6]

list_numbers = []
while True:
    n = input("Enter a number: ")
    if n == 'x':
        break
    else: list_numbers.append(int(n))

repeaters = []

for y in list_numbers:
    if list_numbers.count(y) > 1:
        if repeaters.count(y) == 0:
            repeaters.append(int(y))
else:
    print("The numbers that were repeated are:",(repeaters))




