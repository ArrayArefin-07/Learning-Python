# Convert Decimal number to octal using print() output formatting
# Given:
#
#
# num = 8
# Expected Output:
#
# The octal number of decimal number 8 is 10

num = 8
octal_num = oct(num)
print("The octal number of decimal number", num, "is", octal_num)
# another way
print('%o' % num)