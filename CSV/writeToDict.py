import csv
from pathlib import Path
 



file = open(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب\python course\CSV", 'employees_1.csv'), 'a', newline='')

writeDic = csv.DictWriter(file, ['Name', 'Salary', 'Date'])
writeDic.writerow({'Name': 'ali', 'Salary': '1500', 'Date': '12/4/2024'})
file.close()