#@@@ Strings @@@
#convert an int to a str
aStr = str(3.14)

#concantenate 2 strings together.  Cannot concatenate a string to an integer
#The 3 statements below are the same
print('@@@ Strings @@@')
print('i like the number ' + str(8))
print('i like the number ' + aStr)
print('i like the number ' + '8')
print()

#@@@ Integers @@@
print('@@@ Integers @@@')
anInt = int(8)
print(anInt)
print(8)
#int() is good for casting a string to an integer, like after using input()
aStr2 = input()
print(aStr2 + ' + 1 = ' + str(int(aStr2) + 1))
#int() is also good for rounding floating point numbers
print(int(3.14) + 5)
print()

#@@@ Floats @@@
print('@@@ Floats @@@')
aFloat = float(3.14)
print(aFloat)
print(3.14)
print()

#@@@ Comparing Data Types @@@
print('@@@ Comparing Data Types @@@')
#strings won't equal numbers, but integers will equal floats
print('Does the integer 42 equal the string 42?') 
print(42 == '42')
print('Does the integer 42 equal the float 42.0?') 
print(42 == 42.0)
print('Does the integer 42 equal the float 00042.0000?') 
print(42 == 00042.0000)