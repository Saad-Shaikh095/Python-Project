def show_menu():
    print("\n<----- Welcome to Saad's Expense Tracker ----->")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")

def budget_tracker():
    balance = 0
    expenses = []  # to store expense records with category

    while True:
        show_menu()
        choice = input("Choose an option (1 - 4): ")

        if choice == "1":
            income = float(input("Enter Income Amount: ₹"))
            balance += income
            print(f"₹{income} added. New Balance: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter Expense Amount: ₹"))
            if amount > balance:
                print("Not Enough Balance!")
            else:
                category = input("Enter Expense Category (e.g., Food, Travel, Bills): ")
                balance -= amount
                expenses.append((category, amount))
                print(f"₹{amount} for {category} deducted. New Balance: ₹{balance}")

        elif choice == "3":
            print(f"\nCurrent Balance: ₹{balance}")
            if expenses:
                print("Expense Details:")
                for cat, amt in expenses:
                    print(f"   - ₹{amt} spent on {cat}")
            else:
                print("   No expenses added yet.")

        elif choice == "4":
            print("Exiting Saad's Budget Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

budget_tracker()