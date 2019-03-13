import pprint
# Create a list of dictionaries.
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
'''
Prints the contents of a list or dictionary in Python syntax.
If you save it to a .py file you can import this file and use the variable. 
'''
print(pprint.pformat(cats))
file = open('myCats.py', 'w')
file.write('cats=' + pprint.pformat(cats))
file.close()