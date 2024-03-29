
'''
num2 = int(input("Enter a number : "))
result = 20 / num2
print(result)
print("Done")
'''
'''
try:
    list = [20,0,30]
    result = list[0] / list [3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by Zero is Not Possible")
except IndexError:
    print("Index Error")
finally:
   print("Successful")
'''
""" 
try:
    num1 =int(input("Enter First Number : "))
    num2 =int(input("Enter Second Number : "))
    result = num1 / num2
    print(result)

except(ValueError,ZeroDivisionError):
    print("You have entered incorrect input.")

finally:
    print("Thanks")
"""
def voter (age):
    if age < 18 :
        raise ValueError("Invalid Voter")
    return "You are ALlowed to vote"

try:
    print(voter(17))
except ValueError as e:
    print(e)

