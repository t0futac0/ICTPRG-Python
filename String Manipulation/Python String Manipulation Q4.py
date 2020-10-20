#Write a program that takes in a sentence and counts all of the letter 'a' and 'e' (case insensitive) and outputs the total. 
#For example "Hello how are you there today?" would output "a: 2" and "e: 4".

txt = input("Please enter a sentence." "\n")
a = 0
e = 0

for x in txt.lower():
    if x == "a":
        a += 1
    elif x == "e":
        e += 1
print("a: " + str(a) + " and e: " + str(e))