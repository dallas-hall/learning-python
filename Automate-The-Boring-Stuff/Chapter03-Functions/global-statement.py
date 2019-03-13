def spam():
	# tell the compile that the eggs variable is global and not local, even though it is inside a local code block / scope
	global eggs
	eggs = 'global 1'


def bacon():
	# this is a local variable because of the assignment statement and it is inside a function
	eggs = 'local 2'
	print(eggs)


eggs = 'local 1'
# prints the local because no global defined yet
print(eggs)
spam()
# prints the global because the global was defined inside spam()
print(eggs)
# prints local inside of bacon()
bacon()
# because eggs has been declared global, this assigns to the global variable
eggs = 'global 2'
# prints the global variable eggs
print(eggs)
