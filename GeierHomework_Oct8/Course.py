from Student import Student


class Course:
    def __init__(self, name):
        self.studentList = []
        self.name = name
        return

    def addStudent(self, student):
        self.studentList.append(student)
        return

    def getStudent(self, ID):
        return self.studentList[ID]

    def setStudentTests(self, scores, ID):
        for s in scores:
            self.studentList[ID].addTestScore(s)

    def setStudentExam(self, exam, ID):
        self.studentList[ID].setExam(exam)

    def print(self):
        #Prints header
        print(format(self.name, '^75s'))
        print(format("Student Course Report", '^75s'))
        print()

        #Prints table header
        print(format("First Name", '20s'),
              format("Last Name", '20s'),
              format("Student ID", '20s'),
              format("Semester Avg", '20s'))

        print('=' * 75)

        #Prints Student Information
        for s in self.studentList:
            print(format(s.getFirstName(), '20s'),
                  format(s.getLastName(), '20s'),
                  format(str(s.getStudentID()), '20s'),
                  format(s.getGrade(), '2.2f'))
        print()

# Courses
csCourse = Course("Computer Science")
mathCourse = Course("Mathematics")

# Student Lists
csStudents = [Student("Amy", "Amazing", 0),
              Student("Mike", "Mediocre", 1),
              Student("Sam", "Slacker", 2)]

mathStudents = [Student("Amy", "Amazing", 0),
                Student("Mike", "Mediocre", 1),
                Student("Sam", "Slacker", 2)]

# Test Scores
csScores = [[100, 99, 98],
            [80, 70, 75],
            [50, 40, 20]]

mathScores = [[100, 95],
              [70, 75],
              [50, 60]]

# Exam Scores
csExams = [100, 72, 60]
mathExams = [99, 80, 40]

# Add computer science course data
i = 0
for student in csStudents:
    csCourse.addStudent(student)
    csCourse.setStudentTests(csScores[i], student.getStudentID())
    csCourse.setStudentExam(csExams[i], student.getStudentID())
    i += 1

# Add math course data
i = 0
for student in mathStudents:
    mathCourse.addStudent(student)
    mathCourse.setStudentTests(mathScores[i], student.getStudentID())
    mathCourse.setStudentExam(mathExams[i], student.getStudentID())
    i += 1

# Print course output
csCourse.print()
mathCourse.print()