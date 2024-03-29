# 1 + 2+ 3+ ... + n

n = int(input("Enter the last number : "))

sum  = 0

for x in range (1, n+1, 1) :
    sum = sum + x
print(sum)

print("-------------")

#2+4+6+ ... + n (sum of even numbers from 1-n)

n1 = int(input("Enter the last number : "))

sum1  = 0

for y in range (2, n1+1, 2) :
    sum1 = sum1 + y
print(sum1)

print("--------")
#1+3+5+...+n (sum of odd numbers from 1-n)
n2 = int(input("Enter  the last number : "))

sum2 = 0

for z in range (1, n2+1, 2):
    sum2 = sum2 + z
print(sum2)

#4+8+12....+n
print("----------")
n3 = int(input("Enter  the last number : "))

sum3 = 0

for a in range (4, n3+1, 4):
    sum3 = sum3 + a
print(sum3)

#1*1 + 2*2 + 3*3 + ... + n*n (* indicat squer or to the powe)

print("----------")
n4 = int(input("Enter  the last number : "))

sum4 = 0

for b in range (1, n4+1, 1):
    sum4 = sum4 + b*b
print(sum4)

#2*2 + 4*4 + 6*6 + ... + n*n (* indicat squer or to the powe)

print("----------")
n5 = int(input("Enter  the last number : "))

sum5 = 0

for c in range (2, n5+1, 2):
    sum5 = sum5 + c*c
print(sum5)

# 1 * 2 * 3 * ... * n

print("----------")
n6 = int(input("Enter  the last number : "))

sum6 = 1

for d in range (1, n6+1, 1):
    sum6 = sum6 * d
print(sum6)