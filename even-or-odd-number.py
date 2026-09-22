# Question:Even or Odd Number

# Write a program that asks the user to enter a number.

# Your program should determine whether the number is even or odd.

number  = int(input("Enter a number:    "))
if number   %   2   ==  0:
    print(f"{number} is even")

else:
    print(f"{number} is odd")    