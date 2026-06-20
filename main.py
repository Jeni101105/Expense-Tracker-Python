import csv
def add_expense():

    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid Amount")
        return

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

    print("Expense Added Successfully")

def view_expenses():

    try:
        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            print("\nCategory\tAmount")
            print("-" * 30)

            found = False

            for row in reader:
                found = True
                print(f"{row[0]}\t\t₹{row[1]}")

            if not found:
                print("No expenses found.")

    except FileNotFoundError:
        print("No expenses found.")

def show_total():

    total = 0

    try:
        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:
                total += float(row[1])

        print(f"\nTotal Expense = ₹{total}")

    except FileNotFoundError:
        print("No expenses found.")

def delete_expense():

    expenses = []

    try:
        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:
                expenses.append(row)

    except FileNotFoundError:
        print("No expenses found.")
        return

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\nExpenses:")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense[0]} - ₹{expense[1]}")

    try:
        choice = int(input("\nEnter expense number to delete: "))
    except ValueError:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid Expense Number")
        return

    expenses.pop(choice - 1)

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

    print("Expense Deleted Successfully")

def category_summary():

    summary = {}

    try:
        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                category = row[0]
                amount = float(row[1])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

    except FileNotFoundError:
        print("No expenses found.")
        return

    print("\nCategory Summary")
    print("-" * 30)

    for category, amount in summary.items():
        print(f"{category} : ₹{amount}")

def highest_expense():

    highest_amount = 0
    highest_category = ""

    try:
        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            for row in reader:

                category = row[0]
                amount = float(row[1])

                if amount > highest_amount:
                    highest_amount = amount
                    highest_category = category

    except FileNotFoundError:
        print("No expenses found.")
        return

    if highest_category == "":
        print("No expenses found.")
        return

    print("\nHighest Expense")
    print("-" * 30)
    print(f"{highest_category} : ₹{highest_amount}")

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Delete Expense")
    print("5. Category Summary")
    print("6. Highest Expense")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        category_summary()

    elif choice == "6":
        highest_expense()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")