# Write a program that asks the user for a large number, and then sums all of the digits in that number: 
# Example:
# Enter a large number: 29834892
# Sum of the digits: 2 + 9 + 8 + 3 + 4 + 8 + 9 + 2 = 45

n = input("Please enter a large number ")
digits = ([int(d) for d in str(n)])
total_sum = sum(digits)

print("Sum of digits:", " + " .join(str(n)), " = " , str(total_sum))
