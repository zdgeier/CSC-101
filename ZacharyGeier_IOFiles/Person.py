class Person:
    def __init__(self, first, last, color):
        self.first = first
        self.last = last
        self.color = color

    def __str__(self):
        return str(self.first) + "," + str(self.last) + "," + str(self.color)