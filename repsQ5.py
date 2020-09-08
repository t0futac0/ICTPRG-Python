#Write a program that keeps asking the user for a number, 
# and adds it to a total. Ensure that pressing x stops entering numbers. 
# Example:
#Enter some numbers (Press x to stop):
#1
#3
#66
#x
#Total: 70

total = 0

while True: 
    num = input("Please enter a number ")
    if num != 'x':
        total += int(num)
    else:
        num == 'x'
        break
print(total)