import sqlite3
import csv
from pathlib import Path


#make connection
sqlconnect = sqlite3.connect(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب", 'DataBase.db'))

crsr = sqlconnect.cursor()

sql_command = """create table if not exists employees (
id integer,
Name varchar(20),
Salary integer,
dateOfEmployment text)"""

crsr.execute(sql_command)

#read file

file = open(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب\python course\CSV", 'employees_1 (1).csv'), 'r')
rows = csv.reader(file)

crsr.executemany("insert into employees values (?, ?, ?, ?)", rows)
sqlconnect.commit()
sqlconnect.close()