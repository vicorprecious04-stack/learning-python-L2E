product_name = input("Product name: ")
price = float(input("Price per item: "))
quantity = int(input("Quantity: "))

total_price = price * quantity

print(f"\n========Receipt========")
print(f"Product :  {product_name}")
print(f"Price:  ${price:.2f}")
print(f"Quantity:  {quantity}")
print(f"Total:  ${total_price:.2f}") 
print("-------------------")