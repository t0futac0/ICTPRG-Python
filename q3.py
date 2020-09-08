#Write a program to compare two strings. Get a password from the user. If the password is “Rela238#” accept the password. 
# Otherwise inform the user that the password is incorrect. Set the password using  a variable at the start of the program.

get_username = input("Please enter your username ")
get_password = input("Please enter your password ")
password = str("Rela238#")

if get_password == password:
    print("Password Accepted!")
else:
    print("Password Denied!")