import shelve
path = '/home/dhall/tmp'
filename = 'shelf-file.bin'
# Open the file
file = shelve.open(path + '/' + filename)
# Print the keys and value pairs, need to convert to a list first.
print(list(file.keys()))
print(list(file.values()))
# Read from the file using a map data structure
my_list = file.get('my_list')
file.close()
print(my_list)
