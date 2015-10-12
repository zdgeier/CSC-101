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
        return self.exam

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setTestScores(self, testScores):
        self.__testScores = testScores

    def setExam(self, score):
        self.__exam = score

    def addTestScore(self, score):
        self.__testScores.append(score)

    def getGrade(self):
        testTotal = 0
        for score in self.__testScores:
            testTotal += score

        testAvg = testTotal / len(self.__testScores)

        return exam * 

        return score / len(self.__testScores)

