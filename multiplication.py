# Multiplication Table

# Write a program that asks the user for a number and prints its multiplication table from 1 to 12.
number  = int(input("Enter number:  "))
for i in range(1,13):
    print(f"{number} * {i} = {number * i}")