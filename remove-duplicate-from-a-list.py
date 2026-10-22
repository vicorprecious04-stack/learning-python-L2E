# Remove Duplicates from a List

# You've practised a similar duplicate-removal exercise before, so let's make this one slightly more challenging.

# Given this list:

# numbers = [2, 4, 2, 6, 4, 8, 6, 10, 2, 12, 10]

# Write a program that:

# Creates an empty list called unique_numbers.
# Loops through numbers.
# Checks whether each number is already in unique_numbers.
# Adds the number only if it is not already present.
# Displays the original list and the list without duplicates.

# Expected output:

# Original numbers: [2, 4, 2, 6, 4, 8, 6, 10, 2, 12, 10]
# Unique numbers: [2, 4, 6, 8, 10, 12]
# Rules
# Use a for loop.
# Use an if statement.
# Use .append().
# Do not use set() or remove items directly from the original list.
# Preserve the original order of first appearances.

# Your turn! Write the code yourself and send it to me for review. 💪

numbers = [2, 4, 2, 6, 4, 8, 6, 10, 2, 12, 10]
unique_numbers  = []

for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)

print(unique_numbers)

