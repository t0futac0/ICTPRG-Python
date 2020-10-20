#Write a python script that asks for a username and password, then opens 'logins.txt'
#and tries to find a valid ':' separated login from this file. eg:
#file:
#user4:password3
#python output: username? : user4 password?: password 3 Access Granted!

while True:

    username = input("Enter username: ")
    password = input("Enter password: ")

    for deets in open("logins.txt", "r").readline():
        correctlogin = deets.split(":")  
        if username == correctlogin[0] and password == correctlogin[1]:
            print("Username: ", username, "Password: ", password, "Access Granted")
            break
        else:
            print("Incorrect credentials. Access Denied")
