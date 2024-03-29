'''
import  re
pattern = r"colour"
#match expression
if re.match(pattern,"Colour is a colour, I love red colour"):
    print("Match")
else:
    print("Not Matched")

#search Expression
if re.search(pattern,"Red is a colour, I love red colour"):
    print("Match")
else:
    print("Not Matched")

#findall Expression
print(re.findall(pattern,"Red is a colour, I love red colour"))
'''

'''
import re
pattern = r"colour"
text = "My favourite colour is Red."
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
    '''


import re
pattern = r"colour"
text1 = "My favourite colour is Red. I love blue colour as well"
text2 = re.sub(pattern,"color",text1)
print(text2)



