# Separate Even and Odd Numbers

# Write a program that:

# Asks the user to enter eight numbers.
# Stores all eight numbers in a list called numbers.
# Creates two empty lists: even_numbers and odd_numbers.
# Uses a loop to check each number.
# Adds even numbers to even_numbers and odd numbers to odd_numbers.
# Displays all three lists.

# Example output:

# All numbers: [12, 7, 4, 9, 6, 3, 10, 5]
# Even numbers: [12, 4, 6, 10]
# Odd numbers: [7, 9, 3, 5]

# Rules:

# Use loops.
# Use the modulo operator % to identify even and odd numbers.
# Use .append() to add numbers to the appropriate lists.
# Do not use list comprehensions.

all_numbers = []
even_numbers  = []
odd_numbers = []
for i in range(8):
    items   = int(input(f"Enter numbers {i + 1}: "))
    all_numbers.append(items)
    if items % 2 == 0:
        even_numbers.append(items)

    else:
        odd_numbers.append(items)

print(f"All numbers:    {all_numbers}")
print(f"Even numbers:   {even_numbers}")
print(f"odd numbers:    {odd_numbers}")