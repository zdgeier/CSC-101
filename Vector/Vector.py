class Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        return

    def geti(self):
        return self.i

    def getj(self):
        return self.j

    def seti(self, i):
        self.i = i
        return

    def setj(self, j):
        self.j = j
        return

    def __add__(self, v):
        return Vector(self.i + v.i, self.j + v.j)

    def __sub__(self, v):
        return Vector(self.i - v.i, self.j - v.j)

    def __mul__(self, v):
        return self.i * v.i + self.j * v.j

    def __str__(self):
        return '<' + str(self.i) + ',' + str(self.j) + '>'