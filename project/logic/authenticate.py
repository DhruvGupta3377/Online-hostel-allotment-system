import mysql.connector
import random

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Dhruvgupta.",database="dbms")

def check_password (roll,dob):
    mycursor=mydb.cursor()
    query = "select dob from mytable where rollno = "+ str(roll)
    mycursor.execute(query)
    myrecords=mycursor.fetchall()
    password = myrecords[0][0]
    print (password)
    if int(password) == int(dob):
        return True
    else:
        return False

