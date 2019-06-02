import sqlite3
import pandas as pd

testRecords=[("A","CheesePizza","2000","10","250"),
             ("B","Margarita","4000","9","150"),
             ("C","Mushroom","1200","10","160")]

conn= sqlite3.connect("Pizza.db")
c= conn.cursor()
c.execute('CREATE TABLE Sandwich (code TEXT,name TEXT , calories INTEGER, diameter INTEGER , weight BLOB)')

conn.executemany('Insert into Sandwich VALUES(?,?,?,?,?)',testRecords)
#test
print(pd.read_sql_query("SELECT * FROM Sandwich",conn))