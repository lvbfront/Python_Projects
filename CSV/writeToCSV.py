
import csv
#CSV python library in google
from pathlib import Path

header = ['Name','Salary','Date']
data = [['Hadi',1000,'04/08/2021'], 
        ['Hadi',1000,'04/08/2021'], 
        ['Hadi',1000,'04/08/2021'], 
        ['Hadi',1000,'04/08/2021']]

# file = open(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب\python course\CSV", 'employees_1.csv'), 'w', newline='')

# writer = csv.writer(file)
# writer.writerow(header)
# writer.writerows(data)
# file.close()

file = open(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب\python course\CSV", 'employees_1.csv'), 'w', newline='')
writer = csv.writer(file, delimiter='\t', lineterminator='\n-------------------------------\n')
writer.writerow(header)
writer.writerows(data)
file.close()