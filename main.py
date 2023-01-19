import sqlite3
import datetime

connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()

while (True):
    print("Select an option:\n Enter 1 for a new expense.\n Enter 2 to view expenses summary.\n")

    choice = int(input())
    if choice == 1:
        date =  input("Enter date of expense (YYYY-MM-DD): ")
        description = input("Enter the description of the expense: ")

        cursor.execute("SELECT DISTINCT category FROM expenses")
        categories = cursor.fetchall()

        print("Select a category by number:")
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category[0]}")
        print(f"{len(categories) + 1}. Create a new category")

        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter a new category name: ")
        else:
            category = categories[category_choice - 1][0]
        price = input("Enter the price of expense: ")
        cursor.execute("INSERT INTO expenses (Date, description, category, price) VALUES (?,?,?,?)", (date, description, category, price))
        connection.commit()
    elif choice == 2:
        print("Select an option:\n Enter 1 to view all expenses.\n Enter 2 to view monthly expenses by category.\n")
        view_choice = int(input())
        if view_choice == 1:
           cursor.execute("SELECT * FROM expenses")
           expenses = cursor.fetchall()
           for expense in expenses:
               print(expense)
        elif view_choice == 2:
            month = input("Enter the month (MM): ")
            year = input("Enter the year (YYYY): ")
            cursor.execute("""SELECT category, SUM(price) FROM expenses 
            WHERE strftime('%m', Date) = ? AND strftime('%Y', Date) = ?
            GROUP BY category""", (month, year))
            expenses = cursor.fetchall()
            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]}")
        else:
            exit()
    else:
        exit()

    repeat = input("wanna do something else (y/n)\n")
    if repeat.lower() != "y":
        break

connection.close()

