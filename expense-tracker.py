
print("Welcome to the Expense Tracker! 💼💰")
print("Manage your personal or business expenses in one place! 📊💡")

expenses = []

# Choose the currency once
print("\nChoose a currency:")
print("1. USD")
print("2. EUR")
print("3. RWF")

currency_choice = input("Choose a currency (1-3): ")

if currency_choice == "1":
    currency = "USD"
elif currency_choice == "2":
    currency = "EUR"
elif currency_choice == "3":
    currency = "RWF"
else:
    currency = "RWF"
    print("Invalid choice. Defaulting to RWF.")

print(f"Currency selected: {currency}")

# Main menu
while True:
    print("\nMain Menu")
    print("1. Add an expense 💵")
    print("2. View all expenses 👀")
    print("3. Delete an expense ❌")
    print("4. Calculate total spending 🧮")
    print("5. View totals by category 💡")
    print("6. Exit 👋")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        while True:
            category = input("Enter the expense category (or  'done' to finish): ")

            if category == "done":
                break

            description = input("Describe the expense: ")
            amount = float(input("Enter the amount: "))

            expense = {
                "category": category,
                "description": description,
                "amount": amount
            }

            expenses.append(expense)
            print(f"Expense added successfully! ⚡")
            
    elif choice == "2":
        if len(expenses) == 0:
            print("You haven't added any expenses yet.")
        else:
            print(f"\nYour expenses in {currency}:\n")
            print(f"{'Category':<15} {'Description':<20} {'Amount':>12}")
            print("-" * 50) #tells Python to print 50 dashes in a row to create a horizontal line in your expense table.
            for expense in expenses:
                print(f"{expense['category']:<15} {expense['description']:<20} {expense['amount']:>12}") #- :<15 tells Python to leave space for 15 characters and align the text to the left.
   
    elif choice == "3":
        if len(expenses) == 0:
            print("There are no expenses to delete.")
        else:
            # We use enumerate(expenses, start=1) to number the expenses starting from 1, making it easier for the user to choose.
            for number, expense in enumerate(expenses, start=1):
                print(f"{number}. {expense['category']} - {expense['description']} - {expense['amount']} {currency}")

            to_delete = int(input("Which expense do you want to delete? "))
            expenses.pop(to_delete - 1)
            print("Expense deleted! ❌")

    elif choice == "4":
        total = 0

        for expense in expenses:  # Goes through each expense one by one.
            total += expense["amount"]

        print(f"Total spending💵: {total:,.2f} {currency}")
    
    
    elif choice == "5":
        if len(expenses) == 0:
            print("You haven't added any expenses yet.")
        else:
            # Create an empty dictionary to store totals for each category
            category_totals = {}

            # Go through each expense one by one
            for expense in expenses:
                # Get the category of the current expense
                category = expense["category"]

                # Check if we already have this category in our dictionary
                if category in category_totals:
                    # If it exists, add the new amount to its current total
                    category_totals[category] += expense["amount"]
                else:
                    # If it doesn't exist, create the category and store its amount
                    category_totals[category] = expense["amount"]

            print("\nTotals by category💸:\n")

            # Go through each category and its total
            for category, total in category_totals.items():
                # Display the category, its total, and the chosen currency
                print(f"{category} {total} {currency}")

    elif choice == "6":
            print("Goodbye!👋 Stay organized, and remember : keep a track of where your money goes!💰 💕")
            break


