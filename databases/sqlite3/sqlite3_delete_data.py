import sqlite3

conn = sqlite3.connect('coffee.db')
print("Opened Database!")

conn.execute("DELETE FROM USERS WHERE id=6")

cursor = conn.execute("SELECT * FROM USERS")
for row in cursor:
    print(row)

conn.close()
