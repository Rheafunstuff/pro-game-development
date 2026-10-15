#oop stands for object oriented programming
#objects have features/properties and functions
#before building an object, we build a blueprint

class Student():
    #creating constructor function
    def __init__(self):
        self.name = "Rhea"
        self.age = 11
        self.school = "Upton Court Grammar"
        self.year = "Year 7" 
        self.subjects = ["Maths", "English", "Science", "Computer Science", "Technology"]
        self.scores = []
        self.head_teacher = "Mr King"
    def tests(self):
        for subject in self.subjects:
            score = input(f"Enter the score for {subject}")
            self.scores.append(score)

#creating student objects 
s1 = Student()

#printing properties of object s1
print(s1.name)