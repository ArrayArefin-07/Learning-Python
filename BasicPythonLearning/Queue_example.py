from  collections import deque #import deque

bank = deque(["Anis","Arefin","Oakil"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
if not bank:
    print("No Person left")
