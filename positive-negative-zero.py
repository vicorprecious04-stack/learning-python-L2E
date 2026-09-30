# Positive, Negative, or Zero

# Write a program that asks the user to enter a number.

# Your program should print:

# "Positive" if the number is greater than 0
# "Negative" if the number is less than 0
# "Zero" if the number is exactly 0

number  = int(input("enter a number:    "))
if  number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")