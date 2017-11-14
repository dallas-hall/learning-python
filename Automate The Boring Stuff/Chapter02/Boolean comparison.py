#random Boolean comparison
print('Some random Boolean comparison')
print('Does 42 == 42?')
print(42 == 42)

print('Does \'cat\' == \'dog\'?')
print('cat' == 'dog')

print('Enter your age')
myAge = input()
print('Is your age greater than or equal to 18?')
#remember that input() saves a str so it needs to be converted to an int with int()
print(int(myAge) >= 18)

#De Morgan's law one
print('\nDe Morgan\'s Law')
print('Does not(A or B) == not A and not B?')
A = not(True or True)
B = not True and not True
print(A == B)
#De Morgan's law two
print('Does not(A and B) == not A or not B?')
A = not(True and True)
B = not True or not True
print(A == B)
      
#Truth tables - remember that string concatenation needs to be string to string
print('\nAnd Truth Table')
print('True and True = ' + str(True and True))
print('True and False = ' + str(True and False))
print('False and True = ' + str(False and True))
print('False and False = ' + str(False and False))

print('\nOr Truth Table')
print('True or True = ' + str(True or True))
print('True or False = ' + str(True or False))
print('False or True = ' + str(False or True))
print('False or False = ' + str(False or False))

print('\nExcelusive Or Truth Table')
print('True xor True = ' + str(True ^ True))
print('True xor False = ' + str(True ^ False))
print('False xor True = ' + str(False ^ True))
print('False xor False = ' + str(False ^ False))

print('\nNot And Truth Table')
print('not True and not True = ' + str(not True and not True))
print('not True and not False = ' + str(not True and not False))
print('not False and not True = ' + str(not False and not True))
print('not False and not False = ' + str(not False and not False))

print('\nNot Or Truth Table')
print('not True or not True = ' + str(not True or not True))
print('not True or not False = ' + str(not True or not False))
print('not False or not True = ' + str(not False or not True))
print('not False or not False = ' + str(not False or not False))

print('\nNot Excelusive Or Truth Table')
print('not True xor not True = ' + str(not True ^ not True))
print('not True xor not False = ' + str(not True ^ not False))
print('not False xor not True = ' + str(not False ^ not True))
print('not False xor not False = ' + str(not False ^ not False))