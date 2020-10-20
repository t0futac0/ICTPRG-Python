myFile = open("hello.csv", "r")
names = open("names.txt", "w")
info = myFile.readline().strip()

for line in myFile:
    line = line.strip()
    value = line.split(",")
    if(len(value[0]) > 3):
        names.write(value[0].title())
        names.write("\n")
    print("Name: " + value[0])

names.close()
myFile.close()