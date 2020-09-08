##Write a program that could be used for an (unsecure) login, with a username and password. For example:

##-------------------------------------
##Enter username: bob
##Enter password: password1234
##Access Granted!
##-------------------------------------
##Enter username: frank
##Enter password: invalidpass
##Access Denied!
##-------------------------------------

####Copy and Modify Question 3, to support the following username password combinations:

##bob : password1234
##fred : happyPass122
##lock: passwithlock44
##Please ensure that the password only works with the corresponding username.

get_username = input("Please enter your username ")
get_pass = input("Please enter your password ")
successful = ("Access Granted!")


if get_username == ("bob") and get_pass == ("password1234"):
    print("Access Granted!")
elif get_username == ("fred") and get_pass ==("happyPass122"):
    print (successful)
elif get_username == ("lock") and get_pass==("passwithlock44"):
    print(successful)
    
else:
    print("Invalid combination. Access Denied!")


