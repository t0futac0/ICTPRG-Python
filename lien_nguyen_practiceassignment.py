# Task 1 – Taking Guesses
# Take guesses from the user and display if its greater / less than the random number. Ensure to document your code.
# 	Task 1.1
# 	Allow the user to enter up to 7 guesses. 
# If the user has guessed the number, stop asking for more guesses.
# 	Task 1.2
# 	Show the user if their guess is less than or greater than the random number
# Task 2 – Outputting the result
# Take guesses from the user and display if its greater / less than the random number. Ensure to document your code.
# 	Task 2.1
# 	If the user has guessed the number, display how many guesses it took them
# 	Task 2.2
# 	If the user could not guess the number, call them a fool and show them the number
# Task 3 – Logging guesses
# Display all guesses the user made after they have finished guessing

guess_list=[]
guesses = 0

import random
number = random.randint(0,25)

while guesses < 7:
    print("Guess a number between 1 - 25.")
    guess = input()
    guess = int(guess)
    guess_list.append(int(guess))

    guesses = guesses + 1
    if guess < number:
        print("Your guess is lower than the random number.")
        
    if guess > number:
        print("Your guess is greater than the random number.")
        
    if guess == number:
        break

if guess == number:
    print("It took you", str(guesses), "guesses.","\n" "Your guesses:", list(guess_list))

else:
    if guess != number:
        print("You are a fool! The number is ", str(number), "\n" "Your guesses:", list(guess_list))






  


    
