#a.	Read the specified details from the user (First Name, Last Name, Age)
# This will mean that your application must accept ANY name and age combination not just the ones from the examples.
#b.	Process their age depending on your Student ID
#c.	Generate and output a pipe (‘|’) separated email and password combo.
#i.	This output will be like the example provided, but with the provided name and age used instead.
#d.	Keep asking until the user has entered an empty first name

logins = []

while True:
    first_name = input("First name: ")

    if first_name == (''):
        break
    surname = input("Surname: ")
    user_age = input (str("Age:"))
    student_id_no = 3
    generated_pwd = (int(user_age)) + (int(student_id_no))
    pwdyear = 2020
    pwyear = pwdyear-generated_pwd
    part_1 = first_name[0]
    domain = "@Huawow.io "
    email_address = part_1.lower() + surname.lower() + domain
    seperator = ('| ')
    part_2 = surname[0] 
    initial_password = (first_name.lower() + part_2.upper() + '_' + str(pwyear))
    output = (email_address + seperator + initial_password)
    logins.append(output)
print("Your new login details are: ")

for x in logins:
    print ((x) + '\n' + "* * * * * * * * * * *")





