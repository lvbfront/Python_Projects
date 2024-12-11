import sqlite3
import csv
from pathlib import Path


#make connection
sqlconnect = sqlite3.connect(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب", 'DataBase.db'))

crsr = sqlconnect.cursor()

crsr.execute(" update employees set salary = 1800 where id = 3")  #updating


#deleting
crsr.execute("delete from employees where id = 4")
sqlconnect.commit() #to save changes
sqlconnect.close()