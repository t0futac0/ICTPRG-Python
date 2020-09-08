# This program calculates the sum of a series of number entered.
#decide how many numbers you want
max_nos = 4
# initialise the accumulator variable
sum=0.0
# This program calculates the sum of the numbers you enter
# get the numbers.
for count in range(max_nos):
    num=int(input ("Enter the number: "))
    sum+=num
#Display the total
print("The sum of the numbers is "+str(sum))
