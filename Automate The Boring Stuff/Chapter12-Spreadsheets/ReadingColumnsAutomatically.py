#!/usr/bin/python3

# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
from openpyxl import load_workbook
workbook = load_workbook('../Examples/example.xlsx')

# https://openpyxl.readthedocs.io/en/stable/usage.html#read-an-existing-workbook
worksheet = workbook.active

for i in range(1, 8):
	print(i, worksheet.cell(row=i, column=2).value)

for i in range(1, 8):
	for j in range(1, 4):
		print(str(i) + ',' + str(j), worksheet.cell(row=i, column=j).value)