import sqlite3

conn = sqlite3.connect('coffee.db')
print("Opened Database!")

conn.execute(''' CREATE TABLE USERS
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL); ''')
print('User Table create')

conn.execute("INSERT INTO USERS (ID, NAME) VALUES (1, 'Craig');")
conn.execute("INSERT INTO USERS (ID, NAME) VALUES (2, 'Paul');")
conn.execute("INSERT INTO USERS (ID, NAME) VALUES (3, 'Elma');")
conn.execute("INSERT INTO USERS (ID, NAME) VALUES (4, 'Alice');")
conn.execute("INSERT INTO USERS (ID, NAME) VALUES (5, 'Bob');")
conn.execute("INSERT INTO USERS (ID, NAME) VALUES (6, 'Lauren');")
conn.execute("INSERT INTO USERS (ID, NAME) VALUES (7, 'Annie');")
conn.execute("INSERT INTO USERS (ID, NAME) VALUES (8, 'Gabriel');")

conn.commit()

conn.close()
