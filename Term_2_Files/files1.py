myFile = open("hello.txt", "w")

count = 0
while(count < 10):
    myFile.write(str(count))
    myFile.write("\n")
    count += 1

myFile.close()