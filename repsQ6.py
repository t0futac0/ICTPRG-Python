#Write a program that can output the following shape to the console:
#xxxxx
#xxxxx
#xxxxx
#xxxxx
#xxxxx
#Please ensure that you only have the following print statements within your application:
#print("x", end='')
#print("")
#You will need to use two loops for this to work.

rows = 5
columns = 5

i = 0
while(i < rows):
    j = 0
    while(j < columns):
        print('x', end = '')
        j = j + 1
    i = i + 1
    print()