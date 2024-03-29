#we need to use second brackets{} in Dictionaries

studentId = {
    "101" : "Anisul Islam",
    "102" : "Mobasher Arefin",
    "103" : "Muhammad Oakil Sarker",
    "104" : "Rabby Sadhu",
}
#print(studentId["102"])
print(studentId.get("105"),"Not a valid KEY")