# Write a python script that ask for two numbers, add them together and output the response into a file called 'maths.txt'.

number_1 = int(input("Please enter your first number: "))
number_2 = int(input("Please enter your second number: "))

total = number_1 + number_2

outfile = open('math.txt', 'w')
outfile.write(str(total))
outfile.close()
