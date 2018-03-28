# really useful for printing tabular data formatted data
hexChars = '0123456789ABCDEF'
print('@@@ Justifying @@@')
print('### Original ###')
print(hexChars)
print('\n### Left ###')
# the first argument is how many characters wide the result will be
print(hexChars.ljust(20))
# second argument is what character to pad with
print(hexChars.ljust(20, '*'))
print('\n### Right ###')
print(hexChars.rjust(20))
print(hexChars.rjust(20, '*'))
print('\n### Centre ###')
print(hexChars.center(20))
print(hexChars.center(20, '*'))


def print_table(itemsDictionary, heading, paddingCharacter, leftWidth, rightWidth):
	print('\n' + str(heading).center(leftWidth + rightWidth, paddingCharacter))
	for k, v in itemsDictionary.items():
		print(str(k).ljust(leftWidth, '.') + str(v).rjust(rightWidth))


inventoryItems = {'gold': 10, 'pelts': 3, 'armour': 1}
print_table(inventoryItems, 'Inventory', '-', 10, 5)
