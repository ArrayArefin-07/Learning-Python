# Accept any three string from one input() call
# Write a program to take three names as input from a user in the single input() function call

names = input("Enter three name saperated by space:").split()
print(names)

#another way

str1, str2, str3 = input("Enter Three string:").split()
print(str1)
print(str2)
print(str3)
