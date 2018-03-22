def addToInventory(inventory, addedItems):
	itemsLength = len(addedItems)
	for i in range(itemsLength):
		if addedItems[i] not in inventory.keys():
			inventory[addedItems[i]] = 1
		else:
			inventory[addedItems[i]] = inventory.get(addedItems[i]) + 1
	return inventory


def displayInventory(inventory):
	counter = 0
	for k, v in inventory.items():
		print('You have ' + str(v) + ' ' + str(k) + '.')
		counter += 1
	print('You have ' + str(counter) + ' items.')


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'leather armour', 'dagger']
currentInventory = {'gold coin': 42
	, 'rope': 1
	, 'ruby': 1
					}
currentInventory = addToInventory(currentInventory, dragonLoot)
displayInventory(currentInventory)
