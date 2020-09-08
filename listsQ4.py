#Write a program that enters a string containing a person's full name and then output their initials. Example:

#Full Name: Lachlan van der Velden
#Initials: LVDV
#Full Name: Dave Verg Douglas
#Initials: DVD

initials = ''

full_name = input("Please enter your full name " + '\n')
name_list = full_name.split()

for x in name_list:
    initials += x[0]
    
print("Initials: " + initials.upper(), end='')