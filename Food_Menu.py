print("Welcome to Saad's Python Food Corner..!!")

menu = {
    1: ["Biryani", 200],
    2: ["Chicken 65", 150],
    3: ["Butter Chicken", 300],
    4: ["Chicken Tikka", 150],
    5: ["Roti", 20],
    6: ["Naan", 40],
    7: ["Rice", 50],
    8: ["Salad", 30],
    9: ["Soft Drink/Ice Cream", 20],
    10: ["Coffee/Tea", 15]
}

print("\n Menu of Saad's Food Corner Please Order: ")
for key, item in menu.items():
    print(f"{key}. {item[0]} - ₹{item[1]}")

total = 0
order = input("\nEnter the items you want to order (comma-separated): ")
order_list = order.split(",")

for item_no in order_list:
    item_no = int(item_no.strip())
    if item_no in menu:
        quantity = int(input(f"Enter quantity for {menu[item_no][0]}: "))
        total += menu[item_no][1] * quantity
    else:
        print("Invalid item number...!")

print(f"\nTotal Bill: ₹{total}")
print("Thank you for ordering from Saad's Python Food Corner...!")