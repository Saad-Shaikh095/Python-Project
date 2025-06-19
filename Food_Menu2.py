from datetime import datetime

def save_receipt(order_details, total, discount, final_total):
    from datetime import datetime
    now = datetime.now()
    filename = f"receipt_{now.strftime('%Y%m%d_%H%M%S')}.txt"

   
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("===============================\n")
        file.write("Saad Food Corner\n")
        file.write("-------------------------------\n")
        file.write("Item         Qty    Price\n")
        for item in order_details:
            file.write(f"{item[0]:12} {item[1]:<6} ₹{item[2]}\n")
        file.write("-------------------------------\n")
        file.write(f"Subtotal:           ₹{total}\n")
        file.write(f"Discount:           ₹{discount:.2f}\n")
        file.write(f"Total Bill:         ₹{final_total:.2f}\n")
        file.write("===============================\n")
        file.write("Thank you for dining with us!\n")

    print(f"Receipt saved as: {filename}")


def food_corner():
    menu = {
        1: ["Pizza", 120],
        2: ["Burger", 80],
        3: ["Fries", 50],
        4: ["Cold Drink", 40],
        5: ["Pasta", 100]
    }

    print("\nMenu:")
    for key, item in menu.items():
        print(f"{key}. {item[0]} - ₹{item[1]}")

    total = 0
    order_details = []

    order = input("\nEnter the item numbers you want to order (comma-separated): ")
    order_list = order.split(',')

    for item_no in order_list:
        item_no = int(item_no.strip())
        if item_no in menu:
            item_name = menu[item_no][0]
            item_price = menu[item_no][1]
            quantity = int(input(f"Enter quantity for {item_name}: "))
            item_total = item_price * quantity
            total += item_total
            order_details.append([item_name, quantity, item_total])
        else:
            print("Invalid item number!")

    discount = total * 0.10 if total > 500 else 0
    final_total = total - discount

    # Print receipt on screen
    print("\n==============================")
    print("Saad Food Corner")
    print("------------------------------")
    print("Item         Qty    Price")
    for item in order_details:
        print(f"{item[0]:12} {item[1]:<6} ₹{item[2]}")
    print("------------------------------")
    print(f"Subtotal:           ₹{total}")
    print(f"Discount:           ₹{discount:.2f}")
    print(f"Total Bill:         ₹{final_total:.2f}")
    print("==============================")
    print("Thank you for dining with us!\n")

    # Save to file
    save_receipt(order_details, total, discount, final_total)

# Start the app
print("Welcome to Saad Food Corner....!")
food_corner()
