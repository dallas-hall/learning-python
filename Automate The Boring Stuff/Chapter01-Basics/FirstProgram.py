print('hello world =)')  # print a silly message

# blank lines between code are ignored
# print() prints a blank line
print()
print('enter name...')
myName = input()  # read in user input to a variable, which is always a string

print()
print('enter age...')
myAge = input()

print()
print('hi ' + myName + ' you\'re ' + myAge + ' years old')

print()
print('name entered is this many characters long...')
print(len(myName))  # print the length of a variable
