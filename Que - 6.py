# 'cursor()' can be used to execute SQL queries and fetch the results.
# We use the 'execute()' method of the cursor object to execute SQL statements.

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists etf_database")
mycursor.execute("CREATE TABLE if not exists etf_database.etf_list(id INT PRIMARY KEY, symbol varchar(10), name VARCHAR(100))")
mycursor.execute("insert into etf_database.etf_list values(1,'SPY','SPDR S&P 500 ETF')")
mycursor.execute("insert into etf_database.etf_list values(2,'QQQ','Invesco QQQ Trust')")
mycursor.execute("insert into etf_database.etf_list values(3,'DIA','SPDR Dow Jones Industrial Average ETF')")
mycursor.execute("insert into etf_database.etf_list values(4,'IWM','iShares Russell 2000 ETF')")
mydb.commit()
mydb.close()