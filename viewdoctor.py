import sqlite3 as sql
connection = sql.connect("Hospital.db")
result = connection.execute("SELECT * FROM DOCTORS")
for i in result:
    print("Name", i[0])
    print("Email", i[1])
    print("Qualification", i[2])
    print("Address", i[3])
    print("Phone Number", i[4])