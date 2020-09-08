## Write a program that asks the user for three scores out of 100. 
## It then calculates the average. If the average is greater than 90, congratulate the user. 
## Write a pseudocode before you write the Python program.

## Psuedo code: add score1 + score2 + score3 = total_score
# if average_score > 90 congratulate
# else average_score < 90 unlucky

score1 = int(input("Please enter your first score "))
score2 = int(input("Please enter your second score "))
score3 = int(input("Please enter your third score "))

average_score = (score1+score2+score3)/3

if (average_score > 90):
    print("Congratulations!")
else: 
    print("Unlucky!")
