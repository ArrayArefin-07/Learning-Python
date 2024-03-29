'''
n= 3
*
**
***
'''
n = 3
for i in range(n+1):
    print(i*"*")

print("------------")
'''
n=3 
*
***
***** 
'''
n = 3
for j in range(n+1):
    print((2*j-1)*"*")

print("--------")
'''
   *
  **
 ***
****
'''
n= 5
for k in range(n+1):
    print(" " * (n-k) + "*" * k)