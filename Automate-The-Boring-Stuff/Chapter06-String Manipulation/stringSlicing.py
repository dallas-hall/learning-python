my_name = 'Mr Dallas.'
# print all letters with a for loop on the char array
for i in range(len(my_name)):
	print('my_name[' + str(i) + '] has the char ' + my_name[i])

# print my name only using a slice
print('\n' + my_name[3:9])

# check for chars using in
print('Is Dal in ' + my_name + '? ' + str('Dal' in my_name))
print('Is dal in ' + my_name + '? ' + str('dal' in my_name))

# check for chars using not in
print('Is Dal not in ' + my_name + '? ' + str('Dal' not in my_name))
print('Is dal not in ' + my_name + '? ' + str('dal' not in my_name))
