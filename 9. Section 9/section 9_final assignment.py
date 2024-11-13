class MusicSchool:
    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
		    "Talina": [28, "555-765-452", ["Cello"]],
		    "Eric":   [12, "583-356-223", ["Singing"]]}
            
    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
 
	# Add your methods below this line
    # 
    def print_students_data(self):
        for key in MusicSchool.students:
            self.print_student(key)
            
    def print_student(self, name):
        print(f"Student:{name} is {MusicSchool.students[name][0]} years old and is taking {MusicSchool.students[name][2]}")
        
        
    def add_student(self, name,data):
        MusicSchool.students[name] = data

 
 
 
# Create the instance
MusicSchool = MusicSchool(8, 15000)

 
# Call the methods
MusicSchool.print_students_data() 
MusicSchool.print_student("Gino") 
MusicSchool.add_student("Jack", [60, "562-234-234", ["Piano"]])
 