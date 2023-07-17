import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user= "abc",
    password = "password"
)
print(mydb)
mycursor = mydb.cursor()
#mycursor.execute("insert into OrganizationChart.employees values(1, 'Rishi', 28, 500000, 'rishi@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(2, 'Mark', 34, 1000000, 'mark@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(3, 'John', 32, 300000, 'john@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(4, 'Jenny', 23, 400000, 'jenny@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(5, 'Freya', 24, 800000, 'freya@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(6, 'Jia', 54, 900000, 'jia@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(7, 'Anthony', 30, 1200000, 'anthony@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(8, 'Amit', 37, 1800000, 'amit@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(9, 'Bhushan', 51, 2200000, 'bhushan@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(10, 'Supriya', 22, 800000, 'supriya@gmail.com')")
#mycursor.execute("insert into OrganizationChart.employees values(11, 'Ananya', 24, 600000, 'ananya@gmail.com')")
mycursor.execute("update OrganizationChart.employees SET salary = 600000 where id = 2") # Updated the salary of mark (id=2) to 600000
mycursor.execute("delete from OrganizationChart.employees where id = 5") # deleting 5th row from the 'employees' table contained within 'OrganizationChart.'
mydb.commit()
mydb.close()