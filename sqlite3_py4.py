"""SQLite3 - Query the database"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer1.db')
c = conn.cursor()  # creates database cursor

# query the database
c.execute("SELECT * FROM customers")
# print(c.fetchone())
# print(c.fetchmany(3))
# print(c.fetchall())
# results = c.fetchone()[2]
# print(results[1])
# print(results)

# ------------------
items = c.fetchall()

print()
print("First" + "\tLast" + "\tEmail")
print("______________________________________")
for item in items:
    print(item[0] + '\t' + item[1] + '\t' + item[2])

print()
print("Command executed successfully")
conn.commit()  # commit the executed commands
conn.close()  # close the database connection
