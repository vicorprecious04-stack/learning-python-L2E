#  Shopping List Manager 🛒

# Write a program that allows a user to enter five items they want to buy.

# Store the items in a list and display the complete shopping list.


shopping_list   = []

for i in range(5):
    item  = input(f"Enter item {i + 1}:  ")
    shopping_list.append(item)

print(f"\nYour shopping list: {shopping_list}")




