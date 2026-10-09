# Question 3: Login Authentication

# Write a Python program that checks a user's username and password.

# Requirements:

# Ask the user to enter a username.
# Ask the user to enter a password.
# The correct username is admin.
# The correct password is 1234.
# If both are correct, print Login successful. Welcome!
# If either is incorrect, print Invalid username or password.

# Example 1:

# Enter username: admin
# Enter password: 1234
# Login successful. Welcome!

username    = input("Enter username:    ")
password    = int(input("Enter password:    "))
correct_username  = "admin"
correct_password    = "1234"
if username == correct_username and password  == correct_password:
    print("Login successful. Welcome!")

else:
    print("Invalid username or password")