import csv
from datetime import datetime

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
       print("6.exit")

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
       elif choice == 6:
           print("Good Bye")
           save_expenses(expenses)
           IsExpenseTracker = False
       else:
           print("Enter a valid choice, try again\n")

main()



