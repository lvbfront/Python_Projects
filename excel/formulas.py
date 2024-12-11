import openpyxl
from pathlib import Path

excelfile = openpyxl.load_workbook(Path.home() / Path("C:\\Users\\abdu4\\OneDrive\\سطح المكتب\\python course\\excel", "example.xlsx"))
sheet = excelfile['Sheet1']

sheet['B8'] = '=(sum(B1:B6))'
sheet['B9'] = '=(sum(B1 - B6))'
sheet['B10'] = '=average(B1:B6)'
sheet['B11'] = '=COUNTIF(B1:B6, ">750")'  # how many takes more than 750







#saving the file
excelfile.save(filename= Path.home() / Path("C:\\Users\\abdu4\\OneDrive\\سطح المكتب\\python course\\excel", 'example.xlsx'))