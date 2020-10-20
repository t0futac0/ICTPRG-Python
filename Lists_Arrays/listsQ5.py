#Write a program that can accept many numbers from the user, until they enter an x. Example:
#Enter a number: 5
#Enter a number: 9
#Enter a number: 3
#Enter a number: 12
#Enter a number: x
#You entered: [5, 9, 3, 12]

n_list = []
while True:
    n = input("Enter a number ")
    if n == 'x':
        break
    else: 
        n_list.append(int(n))

print("You entered: ", n_list)

