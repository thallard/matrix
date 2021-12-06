import sys

sys.path.append('../')

from Classes.Matrix import Matrix
from Classes.Vector import Vector

if __name__ == '__main__':
    print('\033[32mVector part (addition)\033[0m')
    v1 = Vector([0, 0])
    v2 = Vector([0, 0])
    v1.add(v2.vector)
    v1.print()

    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    v1.add(v2.vector)
    v1.print()

    v1 = Vector([1, 1])
    v2 = Vector([1, 1])
    v1.add(v2.vector)
    v1.print()

    v1 = Vector([21, 21])
    v2 = Vector([21, 21])
    v1.add(v2.vector)
    v1.print()

    v1 = Vector([-21, 21])
    v2 = Vector([21, -21])
    v1.add(v2.vector)
    v1.print()

    v1 = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v2 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    v1.add(v2.vector)
    v1.print()

    v1 = Vector([-21, 21])
    v2 = Vector([21, -21])
    v1.add(v2.vector)
    v1.print()

    print('\033[32mMatrix part (addition)\033[0m')
    m1 = Matrix([[0, 0], [0, 0]])
    m2 = Matrix([[0, 0], [0, 0]])
    m1.add(m2.matrix)
    m1.print()

    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[0, 0], [0, 0]])
    m1.add(m2.matrix)
    m1.print()

    m1 = Matrix([[1, 1], [1, 1]])
    m2 = Matrix([[1, 1], [1, 1]])
    m1.add(m2.matrix)
    m1.print()

    m1 = Matrix([[21, 21], [21, 21]])
    m2 = Matrix([[21, 21], [21, 21]])
    m1.add(m2.matrix)
    m1.print()

    print('\033[35mVector part (substract)\033[0m')
    v1 = Vector([0, 0])
    v2 = Vector([0, 0])
    v1.sub(v2.vector)
    v1.print()

    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    v1.sub(v2.vector)
    v1.print()

    v1 = Vector([1, 1])
    v2 = Vector([1, 1])
    v1.sub(v2.vector)
    v1.print()

    v1 = Vector([21, 21])
    v2 = Vector([21, 21])
    v1.sub(v2.vector)
    v1.print()

    v1 = Vector([21, 21])
    v2 = Vector([21, 21])
    v1.sub(v2.vector)
    v1.print()

    v1 = Vector([-21, 21])
    v2 = Vector([21, -21])
    v1.sub(v2.vector)
    v1.print()

    v1 = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v2 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    v1.sub(v2.vector)
    v1.print()

    print('\033[35mMatrix part (substract)\033[0m')
    m1 = Matrix([[0, 0], [0, 0]])
    m2 = Matrix([[0, 0], [0, 0]])
    m1.sub(m2.matrix)
    m1.print()

    m1 = Matrix([[1, 0], [0, 1]])
    m2 = Matrix([[0, 0], [0, 0]])
    m1.sub(m2.matrix)
    m1.print()

    m1 = Matrix([[1, 1], [1, 1]])
    m2 = Matrix([[1, 1], [1, 1]])
    m1.sub(m2.matrix)
    m1.print()

    m1 = Matrix([[21, 21], [21, 21]])
    m2 = Matrix([[21, 21], [21, 21]])
    m1.sub(m2.matrix)
    m1.print()

    print('\033[34mVector part (multiply with a scalar)\033[0m')
    v1 = Vector([0, 0])
    v1.scl(1)
    v1.print()

    v1 = Vector([1, 0])
    v1.scl(1)
    v1.print()

    v1 = Vector([1, 1])
    v1.scl(2)
    v1.print()

    v1 = Vector([21, 21])
    v1.scl(2)
    v1.print()

    v1 = Vector([42, 42])
    v1.scl(0.5)
    v1.print()

    print('\033[34mMatrix part (multiply with a scalar)\033[0m')
    m1 = Matrix([[0, 0], [0, 0]])
    m1.scl(0)
    m1.print()

    m1 = Matrix([[1, 0], [0, 1]])
    m1.scl(1)
    m1.print()

    m1 = Matrix([[1, 2], [3, 4]])
    m1.scl(2)
    m1.print()

    m1 = Matrix([[21, 21], [21, 21]])
    m1.scl(0.5)
    m1.print()