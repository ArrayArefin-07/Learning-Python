#set didn't print duplicat value
'''
num1 = {1,2,3,4,5}
num2 = set([4,5,6]) #convert list to set using set()
num2.add(7)         #add element on set list(num2)
num2.remove(5)      #Remove item from set
print(num2)
print(5 in num2)     #checking element in set list
print(5 not in num2) #checking element in set list
'''
num1 = {1,2,3,4,5}
num2 = set([4,5,6])

print(num1 | num2)     # (|) use for union set
print(num1 & num2)     # (&) use for intersection set
print(num1 - num2)     # (-) use for difference of two set



