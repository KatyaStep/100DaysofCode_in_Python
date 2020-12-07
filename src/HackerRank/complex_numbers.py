import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        addition = Complex(0, 0)
        addition.real = self.real + no.real
        addition.imaginary = self.imaginary + no.imaginary

        return addition

    def __sub__(self, no):
        subtraction = Complex(0, 0)
        subtraction.real = self.real - no.real
        subtraction.imaginary = self.imaginary - no.imaginary

        return subtraction

    def __mul__(self, no):
        multiplication = Complex(0, 0)
        multiplication.real = self.real * no.real + self.imaginary * no.imaginary * -1
        multiplication.imaginary = self.real * no.imaginary + self.imaginary * no.real

        return multiplication

    def __truediv__(self, no):
        conjugation = Complex(no.real, -no.imaginary)

        denominatorRes = no * conjugation
        # denominator has only real part
        denominator = denominatorRes.real
        nominator = self * conjugation
        return Complex(nominator.real / denominator, nominator.imaginary / denominator)

    def mod(self):
        a = self.real
        b = self.imaginary

        res = Complex(0, 0)
        res.real = round(math.sqrt(a**2+b**2), 2)
        res.imaginary = 0

        return res

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y,  x.mod(), y.mod()]), sep='\n')
    # , x - y, x * y, x / y, x.mod(), y.mod() ]