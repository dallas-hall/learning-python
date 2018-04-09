import pyperclip
# get the data in the clipboard buffer
pasted_text = pyperclip.paste()
print(pasted_text)

# update the data to add bullet points
pasted_text_lines = pasted_text.split('\n')
for i in range(len(pasted_text_lines)):
	pasted_text_lines[i] = '* ' + pasted_text_lines[i]

print(pasted_text_lines)

# update the data so it can be placed back into the clipboard buffer
pasted_text_update = '\n'.join(pasted_text_lines)
pyperclip.copy(pasted_text_update)
print(pasted_text_update)