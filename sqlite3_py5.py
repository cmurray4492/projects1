"""SQLite3 - Query the database and get row ID"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer1.db')
c = conn.cursor()  # creates database cursor

# query the database
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)


print()
print("Command executed successfully")
conn.commit()  # commit the executed commands
conn.close()  # close the database connection
