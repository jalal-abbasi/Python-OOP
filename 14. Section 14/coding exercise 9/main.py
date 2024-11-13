class Professor:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet_students(self):
        print("Welcome to class!")


# Define your class below this line
class ScienceProfessor(Professor):
    def __init__(self, name, age, course):
        Professor.__init__(self, name, age, course)

    def greet_students(self):
        print("Hi everyone! It's a great day to study science!")
        Professor.greet_students(self)


science_professor = ScienceProfessor("Roberto Corradi", 60, "Dynamics of Mechanical Systems")
science_professor.greet_students()
