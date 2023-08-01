"""First SQLite3 File"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer1.db')

c = conn.cursor()  # creates database cursor

# create a table
c.execute("""CREATE TABLE customers (
          first_name TEXT,
          last_name TEXT,
          email TEXT
)""")

# SQLite3 Datatypes
# NULL
# INTERGER
# REAL
# TEXT
# BLOB

conn.commit()

conn.close()
