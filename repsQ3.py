#Write a program that keeps asking a user for a number, until the number is within the range of 50 and  70. 
#Example:
#Enter a number: 42
#Not within range.
#Enter a number:53
#Within range.

while True:
    num = int(input("Enter number to see if in range \n"))
    if num >= 50 and num <= 70:
        print('Within range.')
    else:
        print('Not within range.')
        break