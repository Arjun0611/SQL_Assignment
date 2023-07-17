# DDL stands for Data Definition Language. It is a subset of SQL used to define and manage the structure of a database.
# CREATE is used to create new database objects such as tables, views, schemas, etc.
# ALTER is used to modify the structure of an existing database objects, such as adding or deleting columns, modifying data types, or changing constraints.
# TRUNCATE is used to remove all rows from a table while keeping the table structure intact.
# DROP is used to delete existing database objects.

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user= "abc",
    password = "password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists OrganizationChart")
mycursor.execute("CREATE TABLE if not exists OrganizationChart.employees (id INT PRIMARY KEY, name VARCHAR(100), age INT, salary DECIMAL(10,2))")
mycursor.execute("ALTER TABLE OrganizationChart.employees ADD COLUMN email VARCHAR(255)")
#mycursor.execute("TRUNCATE TABLE OrganizationChart.employees")
#mycursor.execute("DROP TABLE OrganizationChart.employees")
mydb.commit()
mydb.close()
