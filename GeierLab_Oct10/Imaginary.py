class Imaginary:
    def __init__(self, realpart=0, imagpart=0):
        self.real = realpart
        self.imag = imagpart
        return

    def getreal(self):
        return self.real

    def getimag(self):
        return self.imag

    def __add__(self, z):
        realpart = self.real + z.getreal()
        imagpart = self.imag + z.getimag()
        complexsum = Imaginary(realpart, imagpart)
        return complexsum

    def __mul__(self, z):
        first = self.getreal() * z.getreal()
        second = self.getreal() * z.getimag()
        third = self.getimag() * z.getreal()
        fourth = self.getimag() * self.getimag() * -1
        complexprod = Imaginary(first + fourth, second + third)
        return complexprod

    def __sub__(self, z):
        realpart = self.getimag() - z.getreal()
        imagpart = self.getreal() - z.getimag()
        complexsub = Imaginary(realpart, imagpart)
        return complexsub

    def __str__(self):
        return str(self.real) + ' + ' + str(self.imag) + 'i'

ima = Imaginary(6, 10)
ima2 = Imaginary(6, 10)
print(ima + ima2)
print(ima - ima2)
print(ima * ima2)