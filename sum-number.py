# Sum of Numbers



# Write a program that asks:

# Enter a number:

# Then calculates the sum of every number from 1 up to that number.

number  = int(input("Enter a number:  "))
total = 0
for i in range(1, number + 1):
    total += i
print(f"sum:{total}")
    
    