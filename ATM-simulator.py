# ATM Simulator

# Start your program with:

# balance = 50000

# Display this menu:

# ===== ATM =====

# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# The user chooses an option.

# Requirements

# Option 1 — Check Balance

# Balance: ₦50000

# Option 2 — Deposit

# Ask for an amount and add it to the balance.

# Option 3 — Withdraw

# Ask for an amount.

# If the amount is greater than the balance:

# Insufficient funds

# Otherwise, subtract it from the balance.

# Option 4 — Exit

# Print:

#  Thank you for using the ATM

Balance = 50000
user_pin = int(input("Enter your 4-digit PIN:   "))
original_pin  = 1234



if user_pin  == original_pin:
    print("==========   \nWelcome to the ATM    ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    Choice  = int(input("Enter option 1, 2 , 3 or 4:   "))
    while Choice   != 4:
        if Choice == 1:
            print(f"Your balance: ₦{Balance}")

        elif Choice == 2:
            amount = float(input("Enter amount to deposit:   "))
            Balance += amount

        elif  Choice == 3:
            amount  = float(input("Enter amount to withdraw:   "))

            if amount > Balance:
                print("Insufficient Balance")
        
            elif amount <= Balance:
                Balance -= amount
                print("withdrawal successful")
                print(f"Remaining Balance: ₦{Balance}")

      


        Choice  = int(input("Enter option 1, 2 , 3 or 4:   "))
    

        
    else:
        print("Thank you for using the ATM")

