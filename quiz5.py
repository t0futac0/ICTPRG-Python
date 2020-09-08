##Write a program that can grade a student based upon a percentage grade. Example:
#What was your grade: 99
#You will receive a "High Distinction"
#Please use the following grade table within your application:
#High Distinction 100 - 90
#Distinction 89- 80
#Credit	79 - 70
#Pass 69 - 50
HD_grade= 90
D_grade= 80
C_grade= 70
P_grade= 60

grade = input("What was your grade? ")
message_template = ("You will receive a ")

if int(grade) >= (HD_grade):
    print(message_template + ("High Distinction"))
elif int(grade) >= (D_grade):
    print(message_template + ("Distinction"))
elif int(grade) >= (C_grade):
    print(message_template + ("Credit"))
elif int(grade) >= (P_grade):
    print(message_template + ("Pass"))
else:
    print(message_template + "Fail")
