# 0 to 10
for i in range(10):
	print(str(i))
print()

# 0 to 8, even numbers only.
for i in range(10):
	# skip odd numbers
	if i % 2 == 1:
		continue
	print(str(i))
