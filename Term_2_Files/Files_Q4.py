#Write a python script that outputs the factorial of all numbers from 1 - 10. eg:


# output is after '->'
#1 -> 1
#2 = 1x2 -> 2
#3 = 1x2x3 -> 6
#4 = 1x2x3x4 -> 24

f = open("factorials.txt", "w")

for x in range (1,11):
    output = str(x) + " = 1"
    factorial = 1

    for y in range(1, x + 1):
        factorial *= y
        if y > 1:
            output += ' x ' + str(y)

    output += ' ---> ' + str(factorial)
    f.write(output + "\n")
f.close()