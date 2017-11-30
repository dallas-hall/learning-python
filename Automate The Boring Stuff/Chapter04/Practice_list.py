# create a 2d list
#spam = [['0,0 - file1', '0,1 - attribute', '0,2 - mime'], ['1,0 - file1', '1,1 - attribute', '1,2 - mime']]
#spam = [[3, 3, 3], [1, 2, 3], [1, 1, 1], [2, 3, 4]]
spam = [[],[],[]]
for i in range(10):
    for j in range(3):
        spam[j].append(i)

# print all of list 0
print('\nPrinting all elements of one list')
print(spam[0])
# print individal elemnt of list 0
print('\nPrinting one element')
print(spam[0][0])
# print all lists elements 1 at a time
print('\nPrinting all elements of all lists, one at a time')
for i in range(len(spam)):
    for j in range(len(spam[i])):
        print(spam[i][j])

spam.sort()
print('\nPrinting all elements of all lists, one at a time, after sorting')
for i in range(len(spam)):
    for j in range(len(spam[i])):
        print(spam[i][j])
    # print a new line at the end of each list
    if j == len(spam[j]) - 1:
        print('\n')