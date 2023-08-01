"""SQLite3 - Insert Multiple Records into a table"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer1.db')

c = conn.cursor()  # creates database cursor

many_customers = [('Wes', 'Brown', 'wes@brown.com'),
                  ('Craig', 'Murray', 'craig@murray.com'),
                  ('Elma', 'Murray', 'elma@murray.com')]

c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

print("Command executed successfully")
conn.commit()

conn.close()
