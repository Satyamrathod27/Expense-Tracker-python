📌 Expense Tracker (Python CLI App)

A simple command-line Expense Tracker built using Python.
This project allows users to add, view, and delete expenses, with data saved permanently using a CSV file.

🚀 Features

➕ Add new expenses

📋 View all saved expenses

❌ Delete an expense by number

💾 Automatic data saving using CSV

🛡 Error handling for invalid input

🔁 Data persists even after program restart

🛠 Technologies Used

Python 3

CSV file handling

Lists & Dictionaries

Functions

Exception Handling

📂 Project Structure
expense-tracker/
│
├── expense_tracker.py   # Main Python program
├── expenses.csv         # Auto-created data file
└── README.md            # Project documentation

▶️ How to Run the Project

1️⃣ Install Python (3.x)

2️⃣ Download or clone this repository

3️⃣ Open the project in PyCharm or terminal

4️⃣ Run the program:

python expense_tracker.py

🧠 How It Works

Each expense is stored as:

Amount

Category

Date

Data is saved inside a CSV file like this:

amount,category,date
250,Food,2026-01-30
1200,Rent,2026-01-01


When the program starts, it loads all previous expenses automatically.

🖥 Example Menu
==== Expense Tracker ====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit

📸 Sample Output
Your Expenses:
1. ₹250 | Food | 2026-01-30
2. ₹1200 | Rent | 2026-01-01

📈 What I Learned From This Project

Working with files in Python

Using CSV for data storage

Writing modular functions

Handling user input safely

Building a real-world CLI application

💡 Future Improvements

Monthly expense summary

Category-wise spending report

