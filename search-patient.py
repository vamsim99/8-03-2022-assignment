import sqlite3 as sql
connection = sql.connect("Hospital.db")
getID = input("Enter the Patient id- ")
result = connection.execute("SELECT * FROM PATIENTS WHERE ID="+getID)
print("PATIENT RECORD")
for i in result:
    print("id", i[0])
    print("Name", i[1])
    print("Address", i[2])
    print("Phone Number", i[3])
    print("Email", i[4])
    print("Pincode", i[5])