import shelve
path = '/home/dhall/tmp'
filename = 'shelf-file.bin'
# Open the file
file = shelve.open(path + '/' + filename)
my_list = ['this guy', 'that guy', 'some guy']
# Write to the file using a map data structure
file['my_list'] = my_list
file.close()
