# simple loop
i = 0
while i < 5:
	print(str(i))
	i = i + 1
print()

# create an infinite loop but break it once we get to 10
i = 0
while True:
	print(str(i))
	i = i + 1
	# kill the loop when we get to a multiple of 10
	if i % 10 == 0:
		break
print()

# create an infinite loop but break it once we get to 10, skip every even number
i = 0
while True:
	# skip every even number
	if i % 2 == 0:
		i = i + 1
		continue
	print(str(i))
	i = i + 1
	# kill the loop when we get to a multiple of 10
	if i % 10 == 0:
		break
