myFile = open("hello.txt", "r")

# ------ Read all contents ------
# contents = myFile.read()
# print(contents)

# ------ Reading line by line ------
# line = myFile.readline()
# while(line != ""):
#     print(line)
#     line = myFile.readline()

# ------ Reading line by line using arrays ------
# lines = myFile.readlines()
# while loop
# count = 0
# while(count < len(lines)):
#     print(str(count) + ": " + lines[count])
#     count += 1
# --- for loop ---
# for line in lines:
#     print(line)

# ------ Shorthanded lazy way ------
for line in myFile:
  print(line.strip())

myFile.close()