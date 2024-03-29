# Read line number 4 from the following file
# See:
#
# Read Specific Lines From a File in Python
#Python read file
# Create a test.txt file and add the below content to it.
#
# test.txt file:

with open("test.txt","r") as fp:
    lines = fp.readlines()
    print(lines[3])

#the remove() method removes the specified item.
li = ["arefin","Mobasher","Talha"]
li.remove("Talha",)
print(li)

#The pop() method remove the specified index.
# li.pop(0)
# print(li)

num = [1,2,3,4]
li.extend(num)

print(li)