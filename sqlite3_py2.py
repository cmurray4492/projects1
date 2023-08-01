"""First SQLite3 File"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer1.db')

c = conn.cursor()  # creates database cursor

c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com') ")

print("Command executed successfully")
conn.commit()

conn.close()
