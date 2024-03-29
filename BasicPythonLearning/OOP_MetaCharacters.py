
'''
import re
pattern = r"color..r"

if re.match(pattern,"colour"):
    print("Matched")
    '''
import re
pattern = r"[A-Z]"

if re.match(pattern,"Agggggggghhhhhh"):
    print("Matched")


