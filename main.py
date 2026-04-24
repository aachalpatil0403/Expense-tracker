#Expense Tracker

expensesList=[]
print("Welcome to the Expense Tracker!")

while True:
    print("=== Menu ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    if(choice==1):
       date=input("Enter the date (YYYY-MM-DD): ")
       category=input("Enter the category(food,travel,shopping etc.): ")
       description=input("Enter the description: ")
       amount=float(input("Enter the amount: "))

       expense={
          "date":date,
          "category":category,
          "description":description,
          "amount":amount
        }
       
       expensesList.append(expense) 
       print("Expense added successfully!")


    elif(choice==2):
        if(len(expensesList)==0):
            print("No expenses added yet.")
        else:
            print("==== All Expenses ====")
            count=1
            for expense in expensesList:
                print(f"{count}->{expense['date']} , {expense['category']} , {expense['description']} , {expense['amount']}")
                count=count+1
 
    elif(choice==3):
        total=0
        for expense in expensesList:
            total=total+expense["amount"]
        print("Total Expenses:", total)


    elif(choice==4):
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        