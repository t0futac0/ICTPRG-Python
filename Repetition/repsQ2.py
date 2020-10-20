#Write a program that totals every number between 10 and 50, and outputs the subtotal on a separate line. Example:
#10
#21
#33
#etc...
for i in range (10,51):
    digits = range(10, i+1)
    print(sum(digits))