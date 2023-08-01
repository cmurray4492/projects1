"""SQLite3 - Query the database"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer1.db')

c = conn.cursor()  # creates database cursor

# Query the database
c.execute("SELECT * FROM customers")
print(c.fetchall())


print("Command executed successfully")
conn.commit()

conn.close()
