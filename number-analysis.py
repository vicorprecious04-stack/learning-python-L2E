# Number Analysis

# Write a Python program that asks the user to enter five numbers and then:

# Stores the numbers in a list.
# Calculates the total of all five numbers.
# Calculates their average.
# Finds the largest number.
# Displays the list, total, average, and largest number.

# Rules:

# Use a list to store the numbers.
# Use a loop to calculate the total.
# Do not use sum() or max().
# Convert each input into a number before storing it.



Numbers  = []
Total   = 0
largest = None

for i in range(5):
    item    = int(input(f"Enter number {i + 1}:  "))
    Numbers.append(item)
    Total   += item
    Average = Total / 5

    if largest is None or item > largest:
            largest = item

print(f"\nNumbers:  {Numbers}")
print(f"Total:  {Total}")
print(f"Average:   {Average}")
print(f"Largest:   {largest}")


