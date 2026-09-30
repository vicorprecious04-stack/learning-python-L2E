# Largest of 5

# Write a program that asks the user to enter 5 numbers and finds the largest number.

# Rules:
# Use a loop.
# Do NOT use max().
# Your program should work regardless of the numbers entered.

largest = None
for i in range(1,6):
    number  = int(input(f"Enter number {i}:   "))
    if largest is None or number > largest:
        largest = number
    

print(f"Largest number : {largest} ")        