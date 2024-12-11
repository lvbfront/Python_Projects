import sqlite3
from pathlib import Path

#make connection
sqlconnect = sqlite3.connect(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب", 'DataBase.db'))

crsr = sqlconnect.cursor()
sql_command = """create table if not exists students (
firstName varchar(20),
lastName varchar(20),
age integer)"""

crsr.execute(sql_command)

crsr.execute('insert into students values ("hadi", "Hasan", 23);')
crsr.execute('insert into students values ("Abdo", "Ahmed", 21);')
crsr.execute('insert into students values ("Sara", "Hasan", 22);')

sqlconnect.commit()
sqlconnect.close()
print("done sir!")