# Count Even and Odd Numbers

# Ask the user to enter 5 numbers.

# Your program should count how many are:

# Even
# Odd
even_count   = 0
odd_count   = 0

for i in range(1,6):
    number = int(input(f"Enter number {i}:  "))
    if number % 2 == 0:
        even_count += 1
        

    else:
        odd_count += 1
        

print(f"even numbers:   = {even_count}  ")
print(f"odd numbers:  = {odd_count} ")
