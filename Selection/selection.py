
name= input("Please enter your name ")
reps = int(input("How many times do you want to say your name? "))

#for loop

for x in range(reps):
    print(name)

print ("Loop Complete")

#while -- the variable is incremented / changed IN the loop 

i = 1
while i < 6:
    print("while " + str(i))
    i +=1 

    name = "abc"
    while name != "Tim":
        name = input("Incorrect name - Try again ")
