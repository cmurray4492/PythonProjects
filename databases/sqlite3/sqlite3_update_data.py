import sqlite3

conn = sqlite3.connect('coffee.db')
print("Opened Database!")

conn.execute("UPDATE USERS SET name='Python' WHERE id=4 ")

cursor = conn.execute("SELECT * FROM USERS")
for row in cursor:
    print(row)

conn.close()
