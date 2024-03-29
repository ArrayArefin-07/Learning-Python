# Accept a list of 5 float numbers as an input from the user
# Refer:
#
# Take list as a input in Python.
# Python list
# Expected Output:
#
# [78.6, 78.6, 85.3, 1.2, 3.5]

number = []

for i in range(0,5):
    print("Enter number at location", i , ":")
    item = float(input())
    number.append(item)

print("User List:", number)