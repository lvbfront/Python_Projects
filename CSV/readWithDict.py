
import csv
#CSV python library in google
from pathlib import Path
 



file = open(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب\python course\CSV", 'employees_1.csv'))
DictRead = csv.DictReader(file)

for row in DictRead:
    print(row['Name'], row['Date'], row['Salary'])