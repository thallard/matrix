import sys

sys.path.append('../')

from Classes.Vector import Vector

if __name__ == '__main__':
    v1 = Vector([0, 0, 0])
    print(v1.norm_1(), v1.norm(), v1.norm_inf())

    v1 = Vector([1., 2., 3.])
    print(v1.norm_1(), v1.norm(), v1.norm_inf())

    v1 = Vector([-1, -2])
    print(v1.norm_1(), v1.norm(), v1.norm_inf())
