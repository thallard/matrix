import sys

sys.path.append('../')

from Classes.Vector import Vector

if __name__ == '__main__':
    v1 = Vector([0, 0, 1])
    v2 = Vector([1, 0, 0])
    print(v1.cross_product(v2.vector))

    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print(v1.cross_product(v2.vector))

    v1 = Vector([4, 2, -3])
    v2 = Vector([-2, -5, 16])
    print(v1.cross_product(v2.vector))