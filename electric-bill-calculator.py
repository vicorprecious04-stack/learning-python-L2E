# Electricity Bill Calculator

# You're making excellent progress. Let's move to the next challenge!

# Your task

# Write a Python program that calculates an electricity bill based on the number of units consumed.

# Use these rates:

# Units consumed	Rate per unit
# 0–100 units	₦50
# 101–200 units	₦75
# Above 200 units	₦100

# For this exercise, apply the rate for the relevant band to all units consumed.

# Requirements
# Ask the user to enter the number of electricity units consumed.
# If the units are negative, display Invalid units entered.
# If the units are between 0 and 100, calculate the bill at ₦50 per unit.
# If the units are between 101 and 200, calculate the bill at ₦75 per unit.
# If the units are above 200, calculate the bill at ₦100 per unit.
# Display the total electricity bill.
# Examples

# Example 1:

# Enter units consumed: 80
# Your electricity bill is: ₦4000

units = float(input("Enter units consumed:  "))
if units < 0:
    print("Invalid units")

elif units <=  100:
    print(f"Your electricity bill is: ₦{50 * units}")

elif units <=  200:
    print(f"Your electricity bill is:₦{75 * units}")

else:
    print(f"Your electricity bill is:₦{100 * units}")

