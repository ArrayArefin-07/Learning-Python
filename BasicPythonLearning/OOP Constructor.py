#Uses of Constructor

class student:
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):     #use this for constructor
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = student(101,3.15)
rahim.display()

karim = student(102,3.50)
karim.display()
