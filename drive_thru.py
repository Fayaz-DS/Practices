

print("   Welcome to the Drive-Thru!   ")
print("                                ")
print("         MENU                   ")
print("1. Cheese Burger")
print("2. Fries")
print("3. Soda")
print("4. Ice Cream")
print("5. Cookie")

# Input two items and their quantities
item1 = int(input("Enter the first item number: "))
quantity1 = int(input("How many of item 1?: "))
item2 = int(input("Enter the second item number (or 0 if none): "))
quantity2 = 0
if item2 != 0:
    quantity2 = int(input("How many of item 2?: "))

def get_price(item, quantity):
    prices = {1: 5.99, 2: 2.99, 3: 0.99, 4: 1.49, 5: 3.49}
    return prices.get(item, 0) * quantity

total_price = get_price(item1, quantity1) + get_price(item2, quantity2)

item_names = {1: "Cheese Burger", 2: "Fries", 3: "Soda", 4: "Ice Cream", 5: "Cookie"}
print("\nOrder Summary:")
if item1 in item_names:
    print(f"{quantity1} x {item_names[item1]}")
if item2 != 0 and item2 in item_names:
    print(f"{quantity2} x {item_names[item2]}")
print(f"Total price: ${total_price:.2f}")
print("Thank you for your order!")
    # ...existing code...