import shelve
path = '/home/dhall/tmp'
filename = 'shelf-file.bin'
# Open the file
file = shelve.open(path + '/' + filename)
# Read from the file using a map data structure
my_list = file.get('my_list')
file.close()
print(my_list)
