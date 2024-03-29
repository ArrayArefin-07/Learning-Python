#there are two type of function: Library function and User defined function
#library function : print(), input()

def  add(x,y):   #def is mandatory for creating function
    sum = x + y
    print(sum)

def sub(x,y):
    result = x - y
    print(result)

def message () :
    print("No parameter")

add(10,20)      #call the function with parameter
sub(20,10)      #call the function with parameter
message()