#!/usr/bin/python3

print('# Integer Math')
# Integer math, division always yields a float.
print("2 ** 2 is " + str(2 ** 2))
print("2 * 2 is " + str(2 * 2))
print("2 / 2 is " + str(2 / 2))
print("2 / 3 is " + str(2 / 3))
print("2 // 3 is " + str(2 // 3))
print("2 + 2 is " + str(2 + 2))
print("2 - 2 is " + str(2 - 2))

print('\n# Float Math')
# Float math.
print("0.1 + 0.1 is " + str(0.1 + 0.1))
print("0.1 + 0.2 is " + str(0.1 + 0.2)) # A common addition error in Python.
print("0.2 + 0.2 is " + str(0.2 + 0.2))
print("2 * 0.1 is " + str(2 * 0.1))
print("2 * 0.2 is " + str(2 * 0.2))

print('\n# Large Numbers')
print('The number 2,147,483,648 can be represented in Python as 2_147_483_648 or 2147483648 but not 2,147,483,648.')
two_to_the_thirty_one = 2_147_483_648
print(two_to_the_thirty_one)
