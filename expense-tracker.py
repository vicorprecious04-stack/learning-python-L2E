# Question 6: Expense Tracker
# simple expense-tracking tool for someone who wants to monitor daily spending.

# Requirements
# Write a program that:
# 1. Creates an empty list called expenses.
# 2. Collects five expenses from the user.
# 3. Rejects negative expenses.
# 4. Rejects non-numeric inputs.
# 5. Stores valid expenses in the list.
# 6. Calculates:
#    - Total expenses.
#    - Average expense.
#    - Highest expense.
#    - Lowest expense.
# 7. Displays all the results.

expenses = []
Total_expenses = 0
count = 0

while len(expenses) < 5: 
    while True:
        try:
            users_expense = float(input(f"Enter expenses {len(expenses) + 1}:  "))

            if users_expense < 0:
                 print("Negative values are not allowed. Try again")
                 continue
            
            expenses.append(users_expense)
            break 
        
        except ValueError:
             print("Enter a valid number.")

highest = expenses[0]
lowest = expenses[0]

for i in expenses:
    Total_expenses += i  
    count += 1

    if i > highest:
         highest = i

    if i < lowest:
         lowest = i

average = Total_expenses / count

print("\n--- Summary ---")
print(f"Expenses:         {expenses}")
print(f"Total expenses:   ₦{Total_expenses:,.2f}")
print(f"Average expenses: ₦{average:,.2f}")
print(f"Highest expenses: ₦{highest:,.2f}")
print(f"Lowest expenses:  ₦{lowest:,.2f}")


