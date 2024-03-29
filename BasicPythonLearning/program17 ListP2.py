

subjects = ["C", "C++", "Java", "Python", "BASIC"]



print(len(subjects))  #print length of list

subjects.append("TOC")  #Add iteam on List
print(subjects)

subjects.insert(2,"OS")  #add iteam on specific index
print(subjects)

subjects.remove("BASIC")  #remove item from List
print(subjects)

subjects.sort()  #sort item maintain Dictonary(Asending Like A,B,c)
print(subjects)

subjects.reverse() #SORT item like Decending Order (Like z,y,x)
print(subjects)

subjects.pop()     #remove last iteam from list
subjects.pop()     #remove another last iteam
print(subjects)

#subjects.clear()   #clear all item from subject
#print(subjects)

subjects2 = subjects.copy() # copy item from one list to another list
print(subjects2)

pos = subjects.index("Java")   #print index number of element
print(pos)

pos = subjects.count("Java")   #count use for seeing a element exist how many times
print(pos)



