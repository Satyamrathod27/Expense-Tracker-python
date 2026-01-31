import csv
from datetime import datetime
import matplotlib.pyplot as plt

print("welcome to the Expense tracker")

expense_sheet = "expenses.csv"

def load_expenses():
   expenses = []
   try:
       with open(expense_sheet,"r") as file:
           reader = csv.DictReader(file)

           for row in reader:
               expense = {
                   "amount":float(row["amount"]),
                   "category":row["category"],
                   "date" : row["date"]
               }
               expenses.append(expense)
   except FileNotFoundError:
       print("No previous expense file found. starting fresh.")
   return expenses

def save_expenses(expenses):
   with open(expense_sheet,"w",newline="") as file:
       fieldnames = ["amount","category","date"]
       writer = csv.DictWriter(file ,fieldnames=fieldnames)

       writer.writeheader()
       for expense in expenses:
           writer.writerow(expense)

def add_expense(expenses):
   try:
       amount = float(input("enter the amount: "))
       category = input("enter the category: ")
       date = datetime.today().strftime('%Y-%m-%d')

       expense = {
           "amount":amount,
           "category":category,
           "date":date
       }
       expenses.append(expense)
       save_expenses(expenses)

   except ValueError:
       print("enter the correct value")


def view_expenses(expenses):
   if not expenses:
       print("there are not expenses to track")
       return
   print("\nyour expenses: ")
   for index,exp in enumerate(expenses,start=1):
       print(f"{index}. ${exp['amount']} | {exp['category']} | {exp['date']}")
   print()

def delete_expense(expenses):
   if not expenses:
       print("there are no expenses to delete")
       return
   view_expenses(expenses)
   try:
       choice = int(input("enter the number of the Expense you want to delete: "))
       if 1<= choice <= len(expenses):
           removed = expenses.pop(choice-1)
           save_expenses(expenses)
           print(f"{removed['amount']} {removed['category']} is deleted successfully")
       else:
           print("enter a valid choice")
   except ValueError:
       print("Enter a valid input\n")

def monthly_total(expenses):
   month = input("Enter month(YYYY-MM): ")
   total = 0.0
   for exp in expenses:
       if exp["date"].startswith(month):
           total = total + exp["amount"]
   print(f"total expense of {month}: ${total}")

def filter_date(expenses):
   found = False
   fromdate = input("Enter the From Date(YYYY-MM-DD): ")
   todate = input("Enter the To Date(YYYY-MM-DD): ")
   for exp in expenses:
       date = exp["date"]
       if fromdate <= date <= todate:
           print(f"${exp['amount']} | {exp['category']} | {exp['date']}")
           found = True
   if not found:
       print("There are no Expenses found.\n")
   else:
       print()

def category_report(expenses):
   report = {}
   for exp in expenses:
       category = exp["category"]
       amount = exp["amount"]
       if category in report:
           report[category] += amount
       else:
           report[category] = amount

   for cat, total in report.items():
       print(f"{cat}: ${total}")

def export_monthly_report(expenses):
   month = input("enter the month(YYYY-MM-DD)")
   report = {}

   for exp in expenses:
       date = exp["date"]
       if date.startswith(month):
           cat = exp["category"]
           report[date] = report.get(cat, 0) + exp["amount"]

   filename = f"report {month}.csv"

   with open(filename, "w", newline="") as file:
       writer = csv.writer(file)
       writer.writerow(["Category", "total spent"])

       for cat, total in report.items():
           writer.writerow([cat, total])

   print(f"Report saved as {filename}\n")

def category_search(expenses):
   search = input("enter the category to search: ")
   found = False

   for exp in expenses:
       cat = exp['category']
       if search == cat.lower():
           print(f"{cat}: ${exp['amount']} | {exp['date']}")
           found = True
   if not found:
       print("No Expenses found for this category.\n")
   else:
       print()

def show_category_graph(expenses):
   report = {}

   for exp in expenses:
       cat = exp['category']
       report[cat] = report.get(cat, 0) + exp['amount']

   if not report:
       print("No data to visualize")
       return

   categories = list(report.keys())
   totals = list(report.values())

   plt.bar(categories, totals)
   plt.xlabel("Category")
   plt.ylabel("Amount Spent")
   plt.title("Spending by Category")
   plt.show()

def main():
   expenses = load_expenses()

   IsExpenseTracker = True

   while IsExpenseTracker:
       print("\n====== Expense Tracker Menu ======")
       print("1.add Expense")
       print("2.view expenses")
       print("3.delete expense")
       print("4.Total of this month expense")
       print("5.category report")
       print("6.Apply Date Filter")
       print("7.export monthly report")
       print("8.Search by category")
       print("9.Show Graph of Spending")
       print("10.Exit")

       choice = int(input("choose the option from menu: "))

       if choice == 1:
           add_expense(expenses)
       elif choice == 2:
           view_expenses(expenses)
       elif choice == 3:
           delete_expense(expenses)
       elif choice==4:
           monthly_total(expenses)
       elif choice==5:
           category_report(expenses)
       elif choice==6:
           filter_date(expenses)
       elif choice==7:
           export_monthly_report(expenses)
       elif choice==8:
           category_search(expenses)
       elif choice==9:
           show_category_graph(expenses)
       elif choice == 10:
           print("Good Bye")
           save_expenses(expenses)
           IsExpenseTracker = False
       else:
           print("Enter a valid choice, try again\n")

main()



