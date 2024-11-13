class MusicSchool:
    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
            "Talina": [28, "555-765-452", ["Cello"]],
            "Eric":   [12, "583-356-223", ["Singing"]]}
    def __init__(self, working_hours, revenue):
	    self.working_hours = working_hours
	    self.revenue = revenue
 
	# Add your methods below this line
    def print_students_data(self):
        for key, value in MusicSchool.students.items():
            MusicSchool.print_student(self, key)

    def print_student(self, key):
        if key in MusicSchool.students:
            print(f"Student: {key} who is {MusicSchool.students[key][0]} years old and is taking {MusicSchool.students[key][2]}")
        else:
            print(f"student {key} is not found in our database")

    def add_student(self, name , data):
        MusicSchool.students[name] = data


# Create the instance
school = MusicSchool(8, 15000)

# Call the methods
school.print_students_data()
school.print_student("Jalal")
school.add_student("Jalal", [27,"342-453-323", ["Violen"]])
print(school.students)

# write in file
students = school.students
file2write = open("Students.txt",'w')
file2write.write(str(students))
file2write.close()
