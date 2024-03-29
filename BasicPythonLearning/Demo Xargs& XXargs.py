'''
#xargs

def student (*details):  #use (*) sign for xargs
    print(details)

student(101,"Anis")
student(102,"Arefin",3.75)

print("-----------")
def add(*numbers):
    sum = 0
    for num in  numbers:
        sum = sum+num
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)

'''

#XXargs

def student(**details):   #use (**) sign for xxargs
    print(details)

student(id=101, Name="Anis")




