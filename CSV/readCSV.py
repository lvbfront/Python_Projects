import csv
#CSV python library in google
from pathlib import Path

file = open(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب\python course\CSV", 'employees_1.csv'), 'r')
reader = csv.reader(file)

data = list(reader)
print(data)
#itt workkedddd
#print(data[1] [0])
#print(data[1] [1])

for row in data:
    print('row#' + str(reader.line_num) + ' ' + str(row))