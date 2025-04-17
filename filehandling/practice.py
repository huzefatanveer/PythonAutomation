import os
# os.path.join('usr','bin','spam')
# 'usr/bin/spam'
#
# myFiles = ['accounts.txt','details.csv', 'invite.doc']
# for filename in myFiles:
#     print(os.path.join('/hom/Documents',filename))

# print(os.getcwd())
#
# os.chdir('/usr/bin')
#
# print(os.getcwd())

# os.makedirs('/home/huzefa/Documents/ok')

# print(os.path.abspath('.'))
# print(os.path.isabs('./hi'))
#
# print(os.path.relpath('/home/huzefa/Documents', '/home/huzefa/Desktop'))
# print('/home/huzefa/Desktop'.split(os.path.sep))

# print(os.path.getsize('/home/huzefa/Documents/PythonAutomation'))
# print(os.listdir('/home/huzefa/Documents/PythonAutomation'))

#####
# totalsize = 0
#
# for filename in os.listdir('/home/huzefa/Documents/PythonAutomation'):
#     totalsize = totalsize + os.path.getsize(os.path.join('/home/huzefa/Documents/PythonAutomation', filename))
#     print(totalsize)

file= open("./huz.txt", 'w')

file.write('i am not done yet')
file.close()

file= open('./huz.txt','r')

print(file.read())

file.close()

with open('huz.txt', 'r') as file:
    print(file.read())




