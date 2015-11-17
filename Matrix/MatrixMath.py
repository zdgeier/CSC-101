# Matrix Class Tester - 10/20/15 - Zachary Geier & Katy Mckenzie

from Matrix import Matrix


# Calculates the inverse for 2x2 and 3x3 matrices
def Inverse(matrix):
    if matrix.getRows() == 2 and matrix.getCols() == 2:
        determinant = matrix.determinant()

        #Matrix values
        a = matrix.getEntry(0,0);  b = matrix.getEntry(0,1)
        c = matrix.getEntry(1,0);  d = matrix.getEntry(1,1)

        # Inverse Calculation
        ax = d;       bx = b * -1
        cx = c * -1;  dx = a

        # Sets matrix values
        matrix.setEntry(0, 0, ax);  matrix.setEntry(0, 1, bx)
        matrix.setEntry(1, 0, cx);  matrix.setEntry(1, 1, dx)

        # Final Value
        result = matrix % (1 / determinant)

    elif matrix.getRows() == 3 and matrix.getCols() == 3:
        determinant = matrix.determinant()

        # Matrix Values
        a = matrix.getEntry(0,0);  b = matrix.getEntry(0,1);  c = matrix.getEntry(0,2)
        d = matrix.getEntry(1,0);  e = matrix.getEntry(1,1);  f = matrix.getEntry(1,2)
        g = matrix.getEntry(2,0);  h = matrix.getEntry(2,1);  i = matrix.getEntry(2,2)

        # Inverse Calculation
        ax = (e * i - f * h);  bx = (c * h - b * i);  cx = (b * f - c * e)
        dx = (f * g - d * i);  ex = (a * i - c * g);  fx = (c * d - a * f)
        gx = (d * h - e * g);  hx = (b * g - a * h);  ix = (a * e - b * d)

        # Sets matrix values
        matrix.setEntry(0, 0, ax);  matrix.setEntry(0, 1, bx);  matrix.setEntry(0, 2, cx)
        matrix.setEntry(1, 0, dx);  matrix.setEntry(1, 1, ex);  matrix.setEntry(1, 2, fx)
        matrix.setEntry(2, 0, gx);  matrix.setEntry(2, 1, hx);  matrix.setEntry(2, 2, ix)

        # Final Value
        result = matrix % (1 / determinant)

    return result

# Returns if a solution exists for a matrix (determinant does not equal 0)
def DoesSolutionExist(matrix):
    return matrix.determinant() != 0

# Finds the solution to a system of matrices (inverse of A times C)
def SystemSolution(coefficient, constant):
    return Inverse(coefficient) * constant

# Solves a system of equations and outputs results
def main():
    # Gets coefficient matrix
    print("Input the coefficient matrix: ")
    coeff = Matrix(0,0,m=[])
    coeff.inputMatrix()

    # Gets constant matrix
    print("Input the constant matrix: ")
    const = Matrix(0,0,m=[])
    const.inputMatrix()

    if DoesSolutionExist(coeff):
        sol = SystemSolution(coeff, const)
        print("The solution matrix is:", sol)

        print("The solutions to the system are: ", end='')
        for v in sol.getMatrix():
            print(v, end=' ')

    else:
        print("Solution does not exist!")

main()