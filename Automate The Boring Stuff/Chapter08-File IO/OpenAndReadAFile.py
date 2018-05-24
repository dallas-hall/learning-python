# Both open a file in read only mode and return a File object.
file1 = open('/home/dhall/tmp/distros.txt')
file2 = open('/home/dhall/tmp/brownfox', 'r')

# Read the entire file's data as a String using the File object read function
print('[INFORMATION] Reading entire file in as a string.')
all_file1_string = file1.read()
all_file2_string = file2.read()
# Print out the file contents
print(all_file1_string)
print(all_file2_string)

# Read the file's first line of data as a list using the File object read function
print('[INFORMATION] Reading the file\'s first line as a list.')
# Need to reopen the file.
file1 = open('/home/dhall/tmp/distros.txt')
file2 = open('/home/dhall/tmp/brownfox', 'r')
first_line_file1_string = file1.readline()
first_line_file2_string = file2.readline()
# Print out the file contents
print(first_line_file1_string)
print(first_line_file2_string)

# Read the entire file's data as a list using the File object read function
print('[INFORMATION] Reading entire file in as a list.')
file1 = open('/home/dhall/tmp/distros.txt')
file2 = open('/home/dhall/tmp/brownfox', 'r')
all_file1_list = file1.readlines()
all_file2_list = file2.readlines()
# Print out the file contents
print(all_file1_list)
print(all_file2_list)