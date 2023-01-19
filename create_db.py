import sqlite3

connection = sqlite3.connect("expenses.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY,
Date DATE,
description TEXT,
category TEXT,
price REAL)""")

connection.commit()
connection.close()
