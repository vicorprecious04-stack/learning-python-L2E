# ATM Withdrawal Simulator

# Let's build on your earlier ATM project.

# Requirements

# Write a program that:

# Starts with a balance of ₦50,000.
# Asks the user how much they want to withdraw.
# If the withdrawal amount is greater than the balance, display:
# Insufficient funds.
# If the amount is zero or negative, display:
# Invalid withdrawal amount.
# Otherwise:
# Deduct the withdrawal amount from the balance.
# Display Withdrawal successful!
# Display the remaining balance.
# Example 1: Successful withdrawal
# Enter withdrawal amount: 10000
# Withdrawal successful!
# Remaining balance: ₦40000

balance = 50000
withdrawal_amount   = float(input("Enter withdrawal amount:  "))
if withdrawal_amount > balance:
    print("Insufficient funds")

elif withdrawal_amount <= 0:
    print("Invalid withdrawal amount")

elif withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print("withdrawal successful!")
    print(f"remaining balance:  ₦{balance}")
