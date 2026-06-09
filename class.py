class Classroom:
    def __init__(self, room_name):
        self.room = room_name
        self.teacher = "not assigned yet"
        self.__students = []

    def set_teacher(self, teacher_name):
        self.teacher = teacher_name

    def get_teacher(self):
        return self.teacher

    # Adding students
    def addStudent(self, name, age, course):
        student = {
            "name": name,
            "age": age,
            "course": course
        }
        self.__students.append(student)
        print(name, "has been added successfully")

    # Display all students
    def displayStudents(self):
        if len(self.__students) == 0:
            print("No students found")
        else:
            print("Students in", self.room)
            print("----------------")
            for student in self.__students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("----------------")

    # Search for a student
    def searchStudent(self, name):
        for student in self.__students:
            if student["name"].lower() == name.lower():
                print("Student found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                return
        print("No student found")

    # Update a student's course
    def updateCourse(self, name, new_course):
        for student in self.__students:
            if student["name"].lower() == name.lower():
                student["course"] = new_course
                print(name, "'s course has been updated!")
                return
        print("Student not found. Course was not updated.")

    # Delete a student
    def deleteStudent(self, name):
        for student in self.__students:
            if student["name"].lower() == name.lower():
                self.__students.remove(student)
                print(name, "has been removed.")
                return
        print("Student not found. Nothing was deleted.")

    # Count students
    def countStudents(self):
        return len(self.__students)


# Create classroom
room = Classroom("Classroom 1")

# Set teacher
room.set_teacher("Mahim")

# Add students
room.addStudent("Andre", 12, "Computer Science")
room.addStudent("Shoeib", 12, "Cybersecurity")
room.addStudent("Meet", 12, "IT")

# Display students
room.displayStudents()

# Search for a student
room.searchStudent("Shoeib")

# Update course
room.updateCourse("Shoeib", "Software Development")

# Delete a student
room.deleteStudent("Andre")

# Display students again
room.displayStudents()

# Show teacher and total students
print("Teacher:", room.get_teacher())
print("Total students:", room.countStudents())