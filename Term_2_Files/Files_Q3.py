# Write a python script that reads a file called 'names.txt' (which has names separated by a new line), 
# then converts each name to the correct casing and outputs them to a file called 'names-formated.txt' 
# Eg: lAchlan velDen -> Lachlan Velden
# Frank joe -> Frank Joe
 
f = open("names.txt", "r")
contents = f.read()
print(contents)
f.close()

f = open("names-formatted.txt", "w")
f.write(contents.title())
f.close()
