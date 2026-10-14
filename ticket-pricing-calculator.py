# Ticket Pricing Calculator



# Your task

# Write a Python program that calculates the price of a ticket based on the user's age and student status.

# Ticket prices

# Age group	Ticket price
# Below 13	₦1,000
# 13–17	₦1,500
# 18–59	₦2,500
# 60 and above	₦1,500

# Student discount: Students receive a 20% discount on their ticket price.

# Requirements

# Your program should:

# Ask the user to enter their age.
# Ask whether they are a student (yes or no).
# Reject a negative age with Invalid age.
# Determine the ticket price based on age.
# If the user is a student, deduct 20% from the ticket price.
# Display the final ticket price.



age = int(input("Enter your age:  "))
price  = 0
if age < 0:
    print("Invalid age" )

else:
    student = input("Are you a student? (yes/no):  ").strip().lower()



    if age < 13:
        price = 1000

    elif age <= 17:
        price = 1500

    elif age <= 59:
        price = 2500

    else:
        price = 1500

    if student == "yes":
        price = price * 0.80

    print(f"Your ticket price is:   ₦{price:.0f}")

