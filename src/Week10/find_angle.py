import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        d = list()

    def __sub__(self, no):
        new_point = Points(0, 0, 0)
        new_point.x = self.x - no.x
        new_point.y = self.y - no.y
        new_point.z = self.z - no.z
        return new_point

    def dot(self, no):
        new_point = Points(0,0,0)
        new_point.x = self.x * no.x
        new_point.y = self.y * no.y
        new_point.z = self.z * no.z
        return new_point.x + new_point.y + new_point.z

    def cross(self, no):
        new_point = Points(0, 0, 0)
        new_point.x = (self.y * no.z) - (self.z * no.y)
        new_point.y = -((self.x * no.z) - (self.z * no.x))
        new_point.z = (self.x * no.y) - (self.y * no.x)
        return new_point

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    def __repr__(self):
        return f'{self.x}, {self.y}, {self.z}'


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[ 0 ]), Points(*points[ 1 ]), Points(*points[ 2 ]), Points(*points[ 3 ])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    print(x, y, sep="\n")

    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
