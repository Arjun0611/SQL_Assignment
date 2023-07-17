# Data Query Language is used to retrieve data from a database. DQL allows one to write queries that specify the data one want to retrieve and the conditions that the data must meet.

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user= "abc",
    password = "password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("select * from OrganizationChart.employees")
for i in mycursor.fetchall():
    print(i)