import pprint


#used to format string and we can use those strings in ourcode for execution, to print logs or whatever we want
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import myCats

print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])