# Write a program that takes in 2 values one an email and one a number. 
# Print the email address how ever many times the number says with the count prefixing the number. 
# For example i enter 'bob@example.com' and the number '2', I will get an output of '1_bob@example.com' and then '2_bob@example.com'.

email_addy = input("Enter your email address: ")
num = int(input("How many times do you need it printed?"))

for x in range(num):
    print (str(x + 1),".",email_addy)



