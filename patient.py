import sqlite3 as sql

connection = sql.connect("Hospital.db")
# conn.execute(''' CREATE TABLE PATIENTS(
#                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                 NAME TEXT,
#                 ADDRESS TEXT,
#                 PHNO TEXT,
#                 EMAIL_ID TEXT,
#                 PINCODE INTEGER
# );''')
print("Table Created Successful")
getName = input("Enter  Name: ")
getAdd = input("Enter Address: ")
getPhno = input("Enter Phone number: ")
getEmail = input("Enter the Email ")
getPincode = input("Enter the pincode: ")
connection.execute("INSERT INTO PATIENTS(NAME,ADDRESS,PHNO,EMAIL_ID,PINCODE) VALUES ('"+getName+"','"+getAdd+"','"+getPhno+"','"+getEmail+"','"+getPincode+"')")
connection.commit()
connection.close()
print("inserted sucessfully")



