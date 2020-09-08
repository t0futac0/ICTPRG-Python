#Write a program that ask the user for a random set of characters. 
#If the entered characters length is over 7, print a string made of the middle three characters only

charset = input("Please enter some characters. ")
y = len(charset)

if y > 7:
    middle = charset[len(charset)//2]
    print(str(charset[middle-1]), str(charset[middle]), str(charset[middle+1]))
