class Employee():
    def __init__(self, name, age, job, salary, department):
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary
        self.department = department
        self.performance = [2021, 2022, 2023, 2024]
        self.rating = []

    def give_ratings(self):
        for performance in self.performance:
            rating = input(f"Enter the rating for {performance} ")
            self.rating.append(rating)

    def display_information(self):
        print(f"Hey, I am {self.name}. My age is {self.age} years. I work as {self.job} in {self.department}. My salary is {self.salary}. My years of performance{self.performance}. My ratings are{self.rating}")

e1 = Employee("Tim", 42, "engineer", 50, "IT")

e1.give_ratings()
e1.display_information()

e2 = Employee("Nisha", 21, "money_manager", 45, "Finance")

e2.give_ratings()
e2.display_information()

e3 = Employee("Grace", 37, "doctor", 64, "Hospital")

e3.give_ratings()
e3.display_information()


        
      
    
   



  


   
