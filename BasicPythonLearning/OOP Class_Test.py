
class student:
    roll = ""
    gpa = ""

rahim = student()
#print(isinstance(rahim,student)) #this line for checking the object
rahim.roll=101
rahim.gpa=3.70
print(f"Roll : {rahim.roll}, GPA : {rahim.gpa}")

karim = student()
#print(isinstance(rahim,student)) #this line for checking the object
karim.roll=102
karim.gpa=3.75
print(f"Roll : {karim.roll}, GPA : {karim.gpa}")
