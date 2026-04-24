💰 Expense Tracker (Python CLI)

A simple command-line based Expense Tracker built using Python. 
This project allows users to record, view, and calculate their daily expenses in an organized way.

📌 Features
➕ Add new expenses with:
Date (YYYY-MM-DD)
Category (Food, Travel, Shopping, etc.)
Description
Amount
📋 View all recorded expenses
💵 Calculate total expenses
🚪 Exit the application safely

----🛠️ Technologies Used Python (Core concepts)----
Lists
Dictionaries
Loops
Conditional statements

expense-tracker/
│
├── expense_tracker.py   # Main Python script
└── README.md            # Project documentation

Welcome to the Expense Tracker!
=== Menu ===
1. Add Expense
2. View All Expenses
3. View Total Expenses
4. Exit


📖 How It Works
The program runs in a loop until the user chooses to exit.
Expenses are stored in a list of dictionaries.
Each expense contains:
date
category
description
amount


⚠️ Limitations
Data is not saved permanently (no file/database storage)
All data is lost after exiting the program
No input validation for incorrect formats


*****🔮 Future Improvements*****
Save expenses to a file (CSV/JSON)
Add input validation
Filter expenses by category/date
Add a graphical user interface (GUI)


