books = []
books.append("Learn c")        # keep data on stack
books.append("Learn C++")      # keep data on stack
books.append("learn Java")     # keep data on stack
print(books)

books.pop()
print("Now the top book is : ",books[-1])  #remove data from stack

books.pop()
print("Now the top book is : ",books[-1])  #remove data from stack

books.pop()  #remove data from stack
if not books:
    print("No books left")
