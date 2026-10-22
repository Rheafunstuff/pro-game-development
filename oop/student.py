#oop stands for object oriented programming
#objects have features/properties and functions
#before building an object, we build a blueprint

class Student():
    #creating constructor function
    def __init__(self, name, age, year):
        #setting all the properties of the object - this function gets called automatically when we create the object
        self.name = name
        self.age = age
        self.school = "Upton Court Grammar"
        self.year = year
        self.subjects = ["Maths", "English", "Science", "Computer Science", "Technology"]
        self.scores = []
        self.head_teacher = "Mr King"
    def tests(self):
        for subject in self.subjects:
            score = input(f"Enter the score for {subject} ")
            self.scores.append(score)

#creating student objects 
s1 = Student("Rhea", 11, "Year 7")

#printing properties of object s1
print(s1.name)
print(s1.age)
print(s1.subjects)
print("-" * 50)

#calling functions
s1.tests()
print(s1.scores)

s2 = Student("Rayna", 5, "Year 1")
print(s2.name)
print(s2.age)
print(s2.subjects)
print("-" * 50)

s2.tests()
print(s2.scores)


s3 = Student("Shaivali", 9, "Year 4")
print(s3.name)
print(s3.age)
print(s3.subjects)
print("-" * 50)

s3.tests()
print(s3.scores)


s4 = Student("Kanak", 14, "Year 9")
print(s4.name)
print(s4.age)
print(s4.subjects)
print("-" * 50)


s5 = Student("Jenenia", 12, "Year 8")
print(s5.name)
print(s5.age)
print(s5.subjects)
print("-" * 50)

s6 = Student("Simran", 16, "Year 12")
print(s6.name)
print(s6.age)
print(s6.subjects)
print("-" * 50)
