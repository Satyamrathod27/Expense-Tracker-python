import csv

FILENAME = "expenses.csv"


# ================= LOAD EXPENSES =================
def load_expenses():
    expenses = []
    try:
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "date": row["date"]
                })
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")
    return expenses


# ================= SAVE EXPENSES =================
def save_expenses(expenses):
    with open(FILENAME, "w", newline="") as file:
        fieldnames = ["amount", "category", "date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)


# ================= ADD EXPENSE =================
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!\n")

    except ValueError:
        print("Invalid amount. Please enter a number.\n")


# ================= VIEW EXPENSES =================
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\nYour Expenses:")
    for index, exp in enumerate(expenses, start=1):
        print(f"{index}. ₹{exp['amount']} | {exp['category']} | {exp['date']}")
    print()


# ================= DELETE EXPENSE =================
def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.\n")
        return

    view_expenses(expenses)

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(f"Deleted expense: ₹{removed['amount']} {removed['category']}\n")
        else:
            print("Invalid number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


# ================= MAIN MENU =================
def main():
    expenses = load_expenses()

    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Try again.\n")


# ================= START PROGRAM =================
main()
