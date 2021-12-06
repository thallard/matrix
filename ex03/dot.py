import sys

sys.path.append('../')

from Classes.Vector import Vector

if __name__ == '__main__':
    print('\033[35mDot product with vectors\033[0m')
    v1 = Vector([0, 0])
    v2 = Vector([1, 0])
    print(v1.dot(v2))

    v1 = Vector([1, 1])
    v2 = Vector([1, 1])
    print(v1.dot(v2))

    v1 = Vector([2, 2])
    v2 = Vector([2, 2])
    print(v1.dot(v2))
