"""SQLite3 - ordering results"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer1.db')
c = conn.cursor()  # creates database cursor


# Query with order by
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
c.execute("SELECT rowid, * FROM customers ORDER BY last_name")

items = c.fetchall()

for item in items:
    print(item)


print()
print("Command executed successfully")
conn.commit()  # commit the executed commands
conn.close()  # close the database connection
