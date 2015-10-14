class Student:
    def __init__(self, firstName, lastName, studentID):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__studentID = studentID
        self.__testScores = []
        self.__exam = 0
        return

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getStudentID(self):
        return self.__studentID

    def getTestScores(self):
        return self.__testScores

    def getExam(self):
        return self.__exam

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setExam(self, score):
        self.__exam = score

    def addTestScore(self, score):
        self.__testScores.append(score)

    def getGrade(self):
        testTotal = 0
        for score in self.getTestScores():
            testTotal += score

        testAvg = testTotal / len(self.getTestScores())

        return self.getExam() * .25 +  testAvg * .75

    def __str__ (self):
        return