file_path = '/home/dhall/tmp/python-output.txt'
# Open in write mode, will truncate existing file or create a new file.
file = open(file_path, 'w')
# Need to specify end of line or nothing is written.
file.write('Hello from python.\n')
file.write('I am line two.')
file.close()

# Open in append mode, will append to an existing file or create a new file.
file = open(file_path, 'a')
# Need to specify end of line or nothing is written.
file.write('This is the new text that doesn\'t delete the old text. I don\'t have a newline at the start so I am concatenated to the previous line.\n')
file.write('I am another line! yo.')
file.close()

# Open the file in read mode and get all of its content.
file = open(file_path, 'r')
file_content = file.read()
print(file_content)
file.close()