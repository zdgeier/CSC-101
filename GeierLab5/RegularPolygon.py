import math


class RegularPolygon:

    # Initializes variables
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getN(self):
        return self.__n

    def getSide(self):
        return self.__side

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getPerimeter(self):
        return self.__n * self.__side

    def getArea(self):
        return (self.__n * (self.__side**2)) / (4 * math.tan(math.pi/self.__n))


#Test program
polygons = []
polygons.append(RegularPolygon())
polygons.append(RegularPolygon(6, 4))
polygons.append(RegularPolygon(10, 4, 5.6, 7.8))

for i in range(3):
    print("Polygon " + str(i + 1) + ': ')
    print('\t', "Perimeter:", polygons[i].getPerimeter())
    print('\t', "Area:", polygons[i].getArea(), '\n')