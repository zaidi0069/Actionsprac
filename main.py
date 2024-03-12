class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "StudentsInMLOps"

    def enrollStudents(self, num_students):
        self.total_strength += num_students

    def dropStudents(self, num_students):
        self.total_strength -= num_students
        if self.total_strength < 0:
            self.total_strength = 0

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name

# Example Usage:
mlops_class = StudentsInMLOps()
mlops_class.enrollStudents(10)
#print("Total Strength:", mlops_class.getTotalStrength())  # Output: Total Strength: 10
#print("Class Name:", mlops_class.getClassName())          # Output: Class Name: MLOps
mlops_class.dropStudents(1)
#print("Total Strength after drop:", mlops_class.getTotalStrength())  # Output: Total Strength after drop: 7

#hello
