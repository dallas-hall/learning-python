import os

path = '/home/dhall/tmp'
result = os.listdir(path)
total_size = 0
for i in range(len(result)):
	current_file_path = os.path.join(path + '/' + result[i])
	#print(current_file_path)
	#print(os.path.getsize(current_file_path))
	total_size += os.path.getsize(current_file_path)

print('The total size of ' + path + ' in bytes is:')
print(total_size)
print('The total size of ' + path + ' in kilobytes is:')
print(total_size / 1024)