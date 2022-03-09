import sqlite3 as sql

connection = sql.connect("Hospital.db")
getID = input("Enter the Patient id- ")
connection.execute("DELETE FROM PATIENTS WHERE ID="+getID)
connection.commit()
print("Entry Deleted successfully")
result = connection.execute("SELECT * FROM PATIENTS")
print("deleted succesfully")
for i in result:
    print("id", i[0])
    print("Name", i[1])
    print("Address", i[2])
    print("Phone Number", i[3])
    print("Email", i[4])
    print("Pincode", i[5])