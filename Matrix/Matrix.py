# Matrix Class - 10/19/15 - Zachary Geier & Katy Mckenzie


class Matrix:
    def __init__(self, rows, cols, m):
        if m == 0 or m == []:
            self.matrix = []
            self.rows = 0
            self.cols = 0
        else:
            self.matrix = m
            self.rows = len(m)
            self.cols = len(m[0])

    # Overrides + operator for matrix addition
    def __add__(self, m):
        result = Matrix(self.rows, self.cols, [])

        # Checks if both matrices are the same size
        if self.rows == m.getRows() and self.cols == m.getCols():
            # Populates/Calculates result matrix
            for y in range(len(self.matrix)):
                for x in range(len(self.matrix[y])):
                    val = result.getEntry(y,x) + m.getEntry(y, x)
                    result.setEntry(y,x, val)

        return result

    # Overrides % operator for matrix scalar multiplication
    def __mod__(self, scalar):
        result = []

        for y in range(len(self.matrix)):
            row = []
            for x in range(len(self.matrix[y])):
                row.append(self.matrix[y][x] * scalar)
            result.append(row)

        return Matrix(len(result),len(result[0]), m=result)

    # Overrides * operator for matrix multiplication
    def __mul__(self, m):
        result = []

        # Calculates matrix multiplication values
        for y1 in range(self.rows): # first Row
            row = []
            for x2 in range(m.getCols()): # second Col
                val = 0
                for y2 in range(m.getRows()): # second Row
                    val += self.matrix[y1][y2] * m.getEntry(y2,x2)
                row.append(val)
            result.append(row)
        
        return Matrix(len(result), len(result[0]), m=result)

    # Prompts the user to set all values of a matrix
    def inputMatrix(self):
        self.rows = eval(input("Rows: "))
        self.cols = eval(input("Columns: "))

        for r in range(self.rows):
            temp = []
            for c in range(self.cols):
                # "Enter the value of row x and column y:"
                prompt = ("Enter the value of row "
                            + str(r + 1) + " and column "
                            + str(c + 1) + ": ")

                temp.append(eval(input(prompt)))

            self.matrix.append(temp)
            print()

    # Calculates the determinant of a 2x2 or 3x3 matrix
    def determinant(self):

        if self.rows == 2 and self.cols == 2:
            # Matrix Values
            a = self.matrix[0][0];  b = self.matrix[0][1]
            c = self.matrix[1][0];  d = self.matrix[1][1]

            # Determinant Calculation
            result = (a * d - b * c)

        elif self.rows == 3 and self.cols == 3:
            # Matrix Values
            a = self.matrix[0][0];  b = self.matrix[0][1];  c = self.matrix[0][2]
            d = self.matrix[1][0];  e = self.matrix[1][1];  f = self.matrix[1][2]
            g = self.matrix[2][0];  h = self.matrix[2][1];  i = self.matrix[2][2]

            # Determinant Calculation
            result = (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g))

        return result

    def getEntry(self, row, col):
        return self.matrix[row][col]

    def setEntry(self, row, col, val):
        self.matrix[row][col] = val

    def getMatrix(self):
        return self.matrix

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    # Overrides print method to return a string print out of the matrix
    def __str__(self):
        result = '\n'
        for y in range(self.rows):
            for x in range(self.cols):
                result += format(self.matrix[y][x], '3.3f') + ' '
            result += '\n'
        return result