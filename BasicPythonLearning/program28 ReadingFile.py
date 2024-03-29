file = open("student.txt", "r+")
#print(file.writable())
'''
text = file.read()
print(text)
size = len(text)  #print length of file
print(size)
'''

for line in file:
    print(line)

file.close()