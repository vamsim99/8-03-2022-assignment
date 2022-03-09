import sqlite3 as sql
connection = sql.connect("Hospital.db")
getPhno = input("Enter new Phone Number: ")
getName = input("Enter new Name: ")
getEmail = input("Enter new Email: ")
getQuali = input("Enter new Qualification: ")
getAdd = input("Enter new Address: ")


result = connection.execute("UPDATE DOCTORS SET NAME='"+getName+"',EMAIL_ID='"+getEmail+"',QUALIFICATION='"+getQuali+"',ADDRESS='"+getAdd+"' WHERE PHNO='"+getPhno+"'")
connection.commit()
print("Entry Updated successfully")
result = connection.execute("SELECT * FROM DOCTORS WHERE PHNO='"+getPhno+"'")
print("UPDATED RECORD")
for i in result:
    print("Name", i[0])
    print("Email", i[1])
    print("Qualification", i[2])
    print("Address", i[3])
    print("Phone Number", i[4])