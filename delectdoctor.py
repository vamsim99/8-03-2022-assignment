import sqlite3 as sql
connection = sql.connect("Hospital.db")
getPhno = input("Enter the Phone Number= ")
connection.execute("DELETE FROM DOCTORS WHERE PHNO='"+getPhno+"'")
connection.commit()
print("Entry Deleted successfully")
result = connection.execute("SELECT * FROM DOCTORS")
print("UPDATED RECORD")
for i in result:
    print("Name", i[0])
    print("Email", i[1])
    print("Qualification", i[2])
    print("Address", i[3])
    print("Phone Number", i[4])