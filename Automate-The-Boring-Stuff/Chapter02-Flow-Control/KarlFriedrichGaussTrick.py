print('For loop summing, 1 to 100.')
total = 0
for num in range(101):
	total = total + num
print(total)
debugging = False


def gauss_trick_split_list(end_number):
	print('Single list split into 2, reverse the second list, sum each half together.')
	total = 0
	all_numbers = []
	# If the number amount is odd, prepend a 0
	if end_number % 2 != 0:
		all_numbers.append(0)
	for i in range(end_number):
		all_numbers.append(i + 1)
	# Get the middle of the start list, and split the list in half
	middle = len(all_numbers) // 2
	first_set = all_numbers[0:middle]
	all_numbers.sort(reverse=True)
	second_set = all_numbers[0:middle]
	if debugging:
		print(middle)
		print(all_numbers)
		print(first_set)
		print(second_set)
	# Sum the 2 halves, which is 1 way to do the trick - https://betterexplained.com/articles/techniques-for-adding-the-numbers-1-to-100/
	for i in range(len(first_set)):
		if debugging:
			print(str(first_set[i]) + ' ' + str(second_set[i]))
		total+=(first_set[i] + second_set[i])
	print(total)


def gauss_trick_2_lists(end_number):
	print('Single list duplicated, second list reversed, sum together, divide by 2 at the end.')
	total = 0
	all_numbers = []
	for i in range(end_number):
		all_numbers.append(i + 1)
	list2 = list(all_numbers)
	list2.reverse()
	list_length = len(all_numbers)
	if debugging:
		print(all_numbers)
		print(list2)
		print(list_length)
	for i in range(list_length):
		if debugging:
			print(str(all_numbers[i]) + ' ' + str(list2[i]))
		total += (all_numbers[i] + list2[i])
	# Divide by 2 at the end to get the right answer
	print(total / 2)

# 100 should equal 5050
gauss_trick_split_list(100)
gauss_trick_2_lists(100)
