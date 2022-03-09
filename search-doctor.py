import sqlite3 as sql
connection = sql.connect("Hospital.db")
getName = input("Enter the Name: ")
result = connection.execute("SELECT * FROM DOCTORS WHERE NAME='"+getName+"'")
for i in result:
    print("Name", i[0])
    print("Email", i[1])
    print("Qualification", i[2])
    print("Address", i[3])
    print("Phone Number", i[4])