import sqlite3
import csv
from pathlib import Path


#make connection
sqlconnect = sqlite3.connect(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب", 'DataBase.db'))

crsr = sqlconnect.cursor()

crsr.execute("select * from employees where salary > 1500")
#print(crsr.fetchall())
#print(crsr.fetchone())
#print(crsr.fetchmany(2)) #need just one


answer = crsr.fetchall()
print("the employees salary more than 1500 are: ")
for i in answer:
    print(i[1])