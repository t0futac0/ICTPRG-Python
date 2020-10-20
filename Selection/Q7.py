## Here is a code with many nested –if statements. The indentation is not correct. 
## Rewrite the code such that the program works.
## if score >= A_score:
## print(“your grade is A”)
## else:
## if score >= B_score
## print(‘Your grade is B’)
## else:
## if score >= C_score:
## print(‘your grade is C’)
## else:
## if score >= D_score:
## print(‘Your grade is D’)
## else:
## print(‘your grade is F’)

A_score= 90
B_score= 80
C_score= 70
D_score= 60

score=int(input("Please enter your score "))

if int(score >= A_score):
    print("Your grade is A")
elif int(score >= B_score):
    print("Your grade is B")
elif int(score >= C_score):
    print("Your grade is C")
elif int(score >= D_score):
    print("Your grade is D")
else:
    print("Your grade is F")