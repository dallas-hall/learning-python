#!/usr/bin/python3

# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
from openpyxl import load_workbook
workbook = load_workbook('../Examples/example.xlsx')

# https://openpyxl.readthedocs.io/en/stable/usage.html#read-an-existing-workbook
worksheet = workbook.active
print(worksheet['A1'].value)
print(worksheet['A1'].number_format)

print(worksheet['B1'].value)
print(worksheet['B1'].number_format)

print(worksheet['C1'].value)
print(worksheet['C1'].number_format)


