for i in range(10):
	print(str(i))

for i in range(10):
	# skip odd numbers
	if i % 2 == 1:
		continue
	print(str(i))
