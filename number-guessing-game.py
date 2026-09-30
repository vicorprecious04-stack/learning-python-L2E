

# Create a program with:

# secret_number = 7

# Ask the user to guess the number.

# Requirements
# Keep asking until they guess correctly.

# If their guess is too high, print:

# Too high!

# If their guess is too low, print:

# Too low!

# When they get it right:

# Correct! You guessed the number.


secret_number   = 7
guess_number    = int(input("Guess number:  "))
while  guess_number != secret_number:
    if guess_number >   secret_number:
        print("Too high!")

    else:
        print("Too low!")   

    guess_number    = int(input("Guess number:  "))

print("Correct! You guessed the number")
