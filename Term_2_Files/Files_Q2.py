#Write a python script that keeps asking for names, until they enter an empty name, then creates a file called 'people.txt' 
#and adds names on a separate line.

nlist = []
while True:
    name = input("Please enter a name: ")
    if name == "":
        break
    else:
        nlist.append(name + "\n")

output = open("people.txt", "w")
output.writelines(nlist)
output.close

